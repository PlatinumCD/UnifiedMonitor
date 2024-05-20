#ifndef APPLICATIONMANAGER_H
#define APPLICATIONMANAGER_H

#include <vector>
#include "components/base_component.h"

class ApplicationManager {
public:
    void register_component(BaseComponent* component); // Register a new component
    void parse_data(); // Parse data using all registered components
private:
    std::vector<BaseComponent*> components; // List of all registered components
};

#endif // APPLICATIONMANAGER_H