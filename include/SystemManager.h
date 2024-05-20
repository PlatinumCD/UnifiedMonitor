#ifndef SYSTEMMANAGER_H
#define SYSTEMMANAGER_H

#include <vector>
#include "components/BaseComponent.h"

class SystemManager {
public:
    void registerComponent(BaseComponent* component); // Register a new component
    void parseData(); // Parse data using all registered components
private:
    std::vector<BaseComponent*> components; // List of all registered components
};

#endif // SYSTEMMANAGER_H
