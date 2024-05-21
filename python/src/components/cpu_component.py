import os
from components.base_component import BaseComponent

class CPUComponent(BaseComponent):
    def __init__(self, subcomponents_str=None):
        self.cpu_usages = {}
        self.cpu_energy = {}
        self.subcomponents = {
            'usage': self.parse_cpu_usage,
            'energy': self.parse_cpu_energy
        }
        self.subcomponents_to_parse = subcomponents_str.split(',') if subcomponents_str else self.subcomponents.keys()
        self.sockets = self.detect_sockets()

    def parse_data(self):
        for subcomponent in self.subcomponents_to_parse:
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
                        self.cpu_usages[cpu_id] = {
                            'user': int(parts[1]),
                            'nice': int(parts[2]),
                            'system': int(parts[3]),
                            'idle': int(parts[4]),
                            'iowait': int(parts[5]),
                            'irq': int(parts[6]),
                            'softirq': int(parts[7]),
                            'steal': int(parts[8]) if len(parts) > 8 else 0
                        }

    def parse_cpu_energy(self):
        rapl_base_path = "/sys/class/powercap/intel-rapl"
        if os.path.exists(rapl_base_path):
            for entry in os.listdir(rapl_base_path):
                energy_file_path = os.path.join(rapl_base_path, entry, "energy_uj")
                if os.path.isfile(energy_file_path):
                    with open(energy_file_path, 'r') as file:
                        energy_uj = int(file.read().strip())
                        self.cpu_energy[entry] = {'energy_uj': energy_uj}

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
