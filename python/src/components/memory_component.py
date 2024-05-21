import os
from collections import deque
from components.base_component import BaseComponent

class MemoryComponent(BaseComponent):
    IMPORTANT_KEYS = [
        'MemTotal', 'MemFree', 'MemAvailable', 
        'Buffers', 'Cached', 'SwapTotal', 'SwapFree', 
        'Active', 'Inactive', 'Slab', 'Used'
    ]

    def __init__(self, mem_flags, interval=1, period=20):
        self.interval_update = interval
        self.rolling_period = period  # Keep the rolling average for the specified period
        self.rolling_memory_stats = {}
        self.memory_stats = {}
        self.rolling_memory_rates = {}

        self.subcomponents = {
            'usage': self.parse_memory_usage,
            'rolling_usage': self.update_rolling_usage_rates,
        }

        # Determine subcomponents to parse based on mem_flags
        self.subcomponents_to_parse = []
        if mem_flags['mem_full']:
            self.subcomponents_to_parse = list(self.subcomponents.keys())
        else:
            if mem_flags['mem_usage']:
                self.subcomponents_to_parse.append('usage')
            if mem_flags['mem_rolling_usage']:
                self.subcomponents_to_parse.append('rolling_usage')

    def parse_data(self):
        for subcomponent in self.subcomponents_to_parse:
            if subcomponent == 'rolling_usage' and 'usage' not in self.subcomponents_to_parse:
                self.parse_memory_usage()
            if subcomponent in self.subcomponents:
                self.subcomponents[subcomponent]()

    def parse_memory_usage(self):
        meminfo_path = "/proc/meminfo"
        if os.path.exists(meminfo_path):
            with open(meminfo_path, 'r') as file:
                lines = file.readlines()
                memory_usage = {}
                for line in lines:
                    parts = line.split()
                    key = parts[0].rstrip(':')
                    value = int(parts[1])
                    if key in self.IMPORTANT_KEYS:
                        memory_usage[key] = value
                if 'MemTotal' not in memory_usage or 'MemAvailable' not in memory_usage:
                    return  # We need at least these two keys to derive useful data
                memory_usage['Used'] = memory_usage['MemTotal'] - memory_usage['MemAvailable']
                if 'Used' not in self.rolling_memory_stats:
                    self.rolling_memory_stats = {key: deque(maxlen=self.rolling_period) for key in memory_usage}
                self.update_rolling_list(self.rolling_memory_stats, memory_usage)
                self.memory_stats = memory_usage

    def update_rolling_list(self, rolling_dict, new_data):
        for key, value in new_data.items():
            rolling_dict[key].append(value)

    def update_rolling_usage_rates(self):
        self.rolling_memory_rates = {key: self.calculate_rate(values) for key, values in self.rolling_memory_stats.items()}

    def calculate_rate(self, values):
        if len(values) < 2:
            return 0
        rate = (values[-1] - values[0]) / (len(values) - 1) * self.interval_update
        return round(rate, 5)  # Round to 5 decimal places and ensure it takes 6 characters

    def format_rate(self, rate):
        return f"{rate:6.5f}"  # Format to 6 characters wide with 5 decimal places

    def print_component(self, stream):
        if 'usage' in self.subcomponents_to_parse:
            stream.write("Memory Usage (kB):\n")
            for key, value in self.memory_stats.items():
                stream.write(f"  {key}: {value}\n")

        if 'rolling_usage' in self.subcomponents_to_parse:
            stream.write("\nRolling Memory Usage Rates (kB/s):\n")
            for key, value in self.rolling_memory_rates.items():
                formatted_rate = self.format_rate(value)
                stream.write(f"  {key}: {formatted_rate} kB/s\n")