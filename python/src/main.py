import time
import sys
import csv

from core.monitoring_platform import MonitoringPlatform
from components.cpu_component import CPUComponent
from components.disk_component import DiskComponent
from components.memory_component import MemoryComponent
from components.network_component import NetworkComponent
from utils.argparser import parse_arguments

def main():
    parsed_args = parse_arguments()

    # Determine the stream file name
    platform = MonitoringPlatform(parsed_args.stream_file, parsed_args.record_file)

    # System components
    if any(parsed_args.cpu_flags.values()):
        cpu = CPUComponent(parsed_args.cpu_flags, parsed_args.interval, parsed_args.period)
        platform.register_system_component(cpu)

    if any(parsed_args.mem_flags.values()):
        memory = MemoryComponent(parsed_args.mem_flags, parsed_args.interval, parsed_args.period)
        platform.register_system_component(memory)

    # Placeholder for disk and network components, add conditions when subcomponents are defined
    disk = DiskComponent()
    network = NetworkComponent()

    platform.register_system_component(disk)
    platform.register_system_component(network)

    while True:
        platform.parse_system_data()
        platform.print_data()
        platform.record_data()  # Adding CSV recording
        time.sleep(parsed_args.interval)

if __name__ == "__main__":
    main()