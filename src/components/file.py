#!/usr/bin/env python3

import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError:
        return None

def get_cpu_info():
    cpu_info = {}

    # Get CPU frequency
    cpu_info['CPU Frequencies (MHz)'] = []
    for cpu_id in range(os.cpu_count()):
        freq_path = f'/sys/devices/system/cpu/cpu{cpu_id}/cpufreq/scaling_cur_freq'
        freq = read_file(freq_path)
        if freq:
            cpu_info['CPU Frequencies (MHz)'].append(int(freq) / 1000)

    # Get CPU temperatures
    cpu_info['CPU Temperatures (°C)'] = []
    thermal_base = '/sys/class/thermal/thermal_zone'
    for zone_id in range(10):  # Assuming a maximum of 10 thermal zones
        temp_path = f'{thermal_base}{zone_id}/temp'
        temp = read_file(temp_path)
        if temp:
            cpu_info['CPU Temperatures (°C)'].append(int(temp) / 1000)

    # Get CPU usage from /proc/stat
    cpu_info['CPU Usage'] = {}
    stat_data = read_file('/proc/stat')
    if stat_data:
        for line in stat_data.splitlines():
            if line.startswith('cpu'):
                parts = line.split()
                if len(parts) > 4:
                    core_id = parts[0]
                    user, nice, system, idle = map(int, parts[1:5])
                    total = user + nice + system + idle
                    usage = (total - idle) / total * 100 if total else 0
                    cpu_info['CPU Usage'][core_id] = usage

    # Get energy usage if available
    energy_path = '/sys/class/powercap/intel-rapl/intel-rapl:0/energy_uj'
    energy = read_file(energy_path)
    if energy:
        cpu_info['Energy Consumption (μJ)'] = int(energy)

    return cpu_info

def main():
    cpu_info = get_cpu_info()
    for key, value in cpu_info.items():
        print(f"{key}:")
        if isinstance(value, list):
            for item in value:
                print(f"  - {item}")
        elif isinstance(value, dict):
            for subkey, subvalue in value.items():
                print(f"  - {subkey}: {subvalue:.2f}%")
        else:
            print(f"  {value}")

if __name__ == "__main__":
    main()
