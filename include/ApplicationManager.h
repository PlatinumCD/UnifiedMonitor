#ifndef APPLICATIONMANAGER_H
#define APPLICATIONMANAGER_H

#include <vector>
#include "components/BaseComponent.h"

class ApplicationManager {
public:
    void registerComponent(BaseComponent* component); // Register a new component
    void parseData(); // Parse data using all registered components
private:
    std::vector<BaseComponent*> components; // List of all registered components
};

#endif // APPLICATIONMANAGER_H