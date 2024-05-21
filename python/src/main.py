import time
import os
import argparse
import sys

from monitoring_platform import MonitoringPlatform
from components.cpu_component import CPUComponent
from components.disk_component import DiskComponent
from components.memory_component import MemoryComponent
from components.network_component import NetworkComponent

def main():
    parser = argparse.ArgumentParser(description='Select components and subcomponents to parse and print')
    parser.add_argument('-CPU', type=str, help='Specify CPU subcomponents: -CPU usage,energy,rolling_usage,rolling_energy')
    parser.add_argument('--interval', type=float, default=1, help='Interval in seconds between data collections (default is 1 second)')
    parser.add_argument('--period', type=int, default=1, help='The number of updates used to determine the rolling averages')

    args = parser.parse_args()

    # If no arguments are provided, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    log_file_name = "perf_logs"
    platform = MonitoringPlatform(log_file_name)

    # System components
    cpu = CPUComponent(args.CPU, args.interval, args.period)
    disk = DiskComponent()
    memory = MemoryComponent()
    network = NetworkComponent()

    # Register system components
    platform.register_system_component(cpu)
    platform.register_system_component(disk)
    platform.register_system_component(memory)
    platform.register_system_component(network)

    interval = args.interval  # Interval in seconds

    while True:
        platform.parse_system_data()
        platform.print_data()
        time.sleep(interval)

if __name__ == "__main__":
    main()
