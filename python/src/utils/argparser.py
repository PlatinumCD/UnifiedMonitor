import sys
import argparse
from collections import namedtuple

def parse_arguments():
    parser = argparse.ArgumentParser(description='Select components and subcomponents to parse and print')

    # CPU Flags
    cpu_group = parser.add_argument_group('CPU')
    cpu_group.add_argument('--cpu-full', action='store_true', help='Include all CPU subcomponents')
    cpu_group.add_argument('--cpu-usage', action='store_true', help='Include CPU usage subcomponent')
    cpu_group.add_argument('--cpu-energy', action='store_true', help='Include CPU energy subcomponent')
    cpu_group.add_argument('--cpu-usage-short', action='store_true', help='Include CPU usage (less details) subcomponent')
    cpu_group.add_argument('--cpu-rolling-usage', action='store_true', help='Include CPU rolling usage subcomponent')
    cpu_group.add_argument('--cpu-rolling-energy', action='store_true', help='Include CPU rolling energy subcomponent')
    cpu_group.add_argument('--cpu-rolling-usage-short', action='store_true', help='Include CPU rolling usage (less details) subcomponent')

    # Memory Flags
    mem_group = parser.add_argument_group('MEMORY')
    mem_group.add_argument('--mem-full', action='store_true', help='Include all Memory subcomponents')
    mem_group.add_argument('--mem-usage', action='store_true', help='Include Memory usage subcomponent')
    mem_group.add_argument('--mem-rolling-usage', action='store_true', help='Include Memory rolling usage subcomponent')

    # Disk Flags
    disk_group = parser.add_argument_group('DISK')
    # Add disk-specific arguments here when they are developed

    # Network Flags
    network_group = parser.add_argument_group('NETWORK')
    # Add network-specific arguments here when they are developed

    # Interval and Period
    parser.add_argument('--interval', type=float, default=1, help='Interval in seconds between data collections (default is 1 second)')
    parser.add_argument('--period', type=int, default=10, help='The number of updates used to determine the rolling averages (default is 1)')

    args = parser.parse_args()

    cpu_flags = {
        'cpu_full': args.cpu_full,
        'cpu_usage': args.cpu_usage,
        'cpu_energy': args.cpu_energy,
        'cpu_usage_short': args.cpu_usage_short,
        'cpu_rolling_usage': args.cpu_rolling_usage,
        'cpu_rolling_energy': args.cpu_rolling_energy,
        'cpu_rolling_usage_short': args.cpu_rolling_usage_short,
    }

    mem_flags = {
        'mem_full': args.mem_full,
        'mem_usage': args.mem_usage,
        'mem_rolling_usage': args.mem_rolling_usage,
    }

    # Disk and Network flags can be added similarly when their arguments are defined

    args_dict = vars(args)
    if all(not v for k, v in args_dict.items() if k not in ['interval', 'period']):
        parser.print_help()
        sys.exit(1)
    
    ParsedArgs = namedtuple('ParsedArgs', ['cpu_flags', 'mem_flags', 'interval', 'period'])
    
    return ParsedArgs(cpu_flags, mem_flags, args.interval, args.period)
