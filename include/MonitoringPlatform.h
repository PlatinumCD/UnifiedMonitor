#ifndef MONITORINGPLATFORM_H
#define MONITORINGPLATFORM_H

#include "SystemManager.h"
#include "ApplicationManager.h"

class MonitoringPlatform {
public:
    MonitoringPlatform();
    void registerSystemComponent(BaseComponent* component); // Register a system component
    void registerApplicationComponent(BaseComponent* component); // Register an application component
    void parseSystemData(); // Parse all system data
    void parseApplicationData(); // Parse all application data

private:
    SystemManager systemManager; // Manage system components
    ApplicationManager applicationManager; // Manage application components
};

#endif // MONITORINGPLATFORM_H