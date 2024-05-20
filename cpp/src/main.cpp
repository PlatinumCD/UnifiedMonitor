#include <string>
#include <chrono>
#include <thread>
#include <ctime>

#include "monitoring_platform.h"
#include "components/cpu_component.h"
#include "components/disk_component.h"
#include "components/memory_component.h"
#include "components/network_component.h"

int main() {
    std::string log_file_name = "perf_logs";
    MonitoringPlatform platform(log_file_name);

    // System components
    CPUComponent cpu;
    DiskComponent disk;
    MemoryComponent memory;
    NetworkComponent network;

    // Register system components
    platform.register_system_component(&cpu);
    platform.register_system_component(&disk);
    platform.register_system_component(&memory);
    platform.register_system_component(&network);

    int interval = 1;  // Interval in seconds

    while(1) {
        platform.parse_system_data();

	platform.print_data();

        // Sleep for the given interval
        std::this_thread::sleep_for(std::chrono::seconds(interval));
    }

    return 0;
}
