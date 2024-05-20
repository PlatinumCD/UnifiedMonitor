#include "MonitoringPlatform.h"
#include "components/CPUComponent.h"
#include "components/DiskComponent.h"
#include "components/MemoryComponent.h"
#include "components/NetworkComponent.h"

int main() {
    MonitoringPlatform platform;

    // System components
    CPUComponent cpu;
    DiskComponent disk;
    MemoryComponent memory;
    NetworkComponent network;

    // Register system components
    platform.registerSystemComponent(&cpu);
    platform.registerSystemComponent(&disk);
    platform.registerSystemComponent(&memory);
    platform.registerSystemComponent(&network);

/*
    // Register application components
    platform.registerApplicationComponent(&memory);
    platform.registerApplicationComponent(&network);
*/

    // Parse the data
    platform.parseSystemData();

//    platform.parseApplicationData();

    return 0;
}
