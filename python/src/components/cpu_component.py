import os
from components.base_component import BaseComponent
from collections import deque

class CPUComponent(BaseComponent):
    def __init__(self, subcomponents_str=None, interval=1, period=20):
        self.interval_update = interval
        self.rolling_period = period  # For example, keep the rolling average for last 60 seconds
        self.rolling_cpu_usages = {}
        self.rolling_cpu_energy = {}
        self.cpu_usages = {}
        self.cpu_energy = {}
        self.rolling_cpu_rates = {}
        self.rolling_energy_rates = {}
        self.subcomponents = {
            'usage': self.parse_cpu_usage,
            'energy': self.parse_cpu_energy,
            'rolling_usage': self.update_rolling_usage_rates,
            'rolling_energy': self.update_rolling_energy_rates
        }
        self.subcomponents_to_parse = subcomponents_str.split(',') if subcomponents_str else self.subcomponents.keys()
        self.sockets = self.detect_sockets()

    def parse_data(self):
        for subcomponent in self.subcomponents_to_parse:
            if subcomponent == 'rolling_usage' and 'usage' not in self.subcomponents_to_parse:
                self.parse_cpu_usage()
            if subcomponent == 'rolling_energy' and 'energy' not in self.subcomponents_to_parse:
                self.parse_cpu_energy()
            if subcomponent in self.subcomponents:
                self.subcomponents[subcomponent]()

    def detect_sockets(self):
        """
        Detects the number of CPU sockets.
        """
        socket_count = 0
        cpu_info_path = "/proc/cpuinfo"
        if os.path.exists(cpu_info_path):
            with open(cpu_info_path, 'r') as file:
                for line in file:
                    if line.startswith("physical id"):
                        socket_id = int(line.split(':')[1].strip())
                        if socket_id + 1 > socket_count:
                            socket_count = socket_id + 1
        return socket_count

    def parse_cpu_usage(self):
        stat_path = "/proc/stat"
        if os.path.exists(stat_path):
            with open(stat_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("cpu"):
                        parts = line.split()
                        cpu_id = parts[0]
                        if cpu_id == "cpu":
                            continue
                        usage_stats = {
                            'user': int(parts[1]),
                            'nice': int(parts[2]),
                            'system': int(parts[3]),
                            'idle': int(parts[4]),
                            'iowait': int(parts[5]),
                            'irq': int(parts[6]),
                            'softirq': int(parts[7]),
                            'steal': int(parts[8]) if len(parts) > 8 else 0
                        }
                        if cpu_id not in self.rolling_cpu_usages:
                            self.rolling_cpu_usages[cpu_id] = {key: deque(maxlen=self.rolling_period) for key in usage_stats}
                        self.update_rolling_list(self.rolling_cpu_usages[cpu_id], usage_stats)
                        self.cpu_usages[cpu_id] = usage_stats

    def parse_cpu_energy(self):
        rapl_base_path = "/sys/class/powercap/intel-rapl"
        if os.path.exists(rapl_base_path):
            for entry in os.listdir(rapl_base_path):
                energy_file_path = os.path.join(rapl_base_path, entry, "energy_uj")
                if os.path.isfile(energy_file_path):
                    with open(energy_file_path, 'r') as file:
                        energy_uj = int(file.read().strip())
                        if entry not in self.rolling_cpu_energy:
                            self.rolling_cpu_energy[entry] = deque(maxlen=self.rolling_period)
                        self.rolling_cpu_energy[entry].append(energy_uj)
                        self.cpu_energy[entry] = {'energy_uj': energy_uj}

    def update_rolling_list(self, rolling_dict, new_data):
        for key, value in new_data.items():
            rolling_dict[key].append(value)

    def update_rolling_usage_rates(self):
        self.rolling_cpu_rates = {cpu: {key: self.calculate_rate(values) for key, values in usage.items()} for cpu, usage in self.rolling_cpu_usages.items()}

    def update_rolling_energy_rates(self):
        self.rolling_energy_rates = {key: self.calculate_rate(values) for key, values in self.rolling_cpu_energy.items()}

    def calculate_rate(self, values):
        if len(values) < 2:
            return 0
        rate = (values[-1] - values[0]) / len(values) * (1/self.interval_update)
        return round(rate, 5)  # Round to 5 decimal places and ensure it takes 6 characters

    def format_rate(self, rate):
        return f"{rate:6.5f}"  # Format to 6 characters wide with 5 decimal places

    def print_component(self, stream):
        if 'usage' in self.subcomponents_to_parse:
            stream.write("CPU Usage:\n")
            for cpu, usage in self.cpu_usages.items():
                stream.write(f"{cpu}:\n")
                for key, value in usage.items():
                    stream.write(f"  {key}: {value}\n")

        if 'energy' in self.subcomponents_to_parse:
            stream.write(f"\nNumber of CPU Sockets: {self.sockets}\n")
            stream.write("CPU Energy Consumption (μJ):\n")
            for key, value in self.cpu_energy.items():
                stream.write(f"  {key}: {value['energy_uj']} μJ\n")

        if 'rolling_usage' in self.subcomponents_to_parse:
            stream.write("\nRolling CPU Usage Rates:\n")
            for cpu, usage in self.rolling_cpu_rates.items():
                stream.write(f"{cpu}:\n")
                for key, value in usage.items():
                    formatted_rate = self.format_rate(value)
                    stream.write(f"  {key}: {formatted_rate}\n")
        
        if 'rolling_energy' in self.subcomponents_to_parse:
            stream.write("\nRolling CPU Energy Consumption Rates (μJ/s):\n")
            for key, value in self.rolling_energy_rates.items():
                formatted_rate = self.format_rate(value)
                stream.write(f"  {key}: {formatted_rate} μJ/s\n")
