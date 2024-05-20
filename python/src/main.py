import time
import os

from monitoring_platform import MonitoringPlatform
from components.cpu_component import CPUComponent
from components.disk_component import DiskComponent
from components.memory_component import MemoryComponent
from components.network_component import NetworkComponent

def main():
    log_file_name = "perf_logs"
    platform = MonitoringPlatform(log_file_name)

    # System components
    cpu = CPUComponent()
    disk = DiskComponent()
    memory = MemoryComponent()
    network = NetworkComponent()

    # Register system components
    platform.register_system_component(cpu)
    platform.register_system_component(disk)
    platform.register_system_component(memory)
    platform.register_system_component(network)

    interval = 1  # Interval in seconds

    while True:
        platform.parse_system_data()
        platform.print_data()
        time.sleep(interval)

if __name__ == "__main__":
    main()