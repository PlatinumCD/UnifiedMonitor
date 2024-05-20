#include "MonitoringPlatform.h"
#include "SystemManager.h"
#include "ApplicationManager.h"

MonitoringPlatform::MonitoringPlatform() {
}

void MonitoringPlatform::registerSystemComponent(BaseComponent* component) {
    systemManager.registerComponent(component);  // Register the system component with the system manager
}

void MonitoringPlatform::registerApplicationComponent(BaseComponent* component) {
    applicationManager.registerComponent(component);  // Register the application component with the application manager
}

void MonitoringPlatform::parseSystemData() {
    systemManager.parseData();  // Parse data for all registered system components
}

void MonitoringPlatform::parseApplicationData() {
    applicationManager.parseData();  // Parse data for all registered application components
}
