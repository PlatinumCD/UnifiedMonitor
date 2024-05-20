#ifndef SYSTEMMANAGER_H
#define SYSTEMMANAGER_H

#include <vector>
#include "components/base_component.h"

class SystemManager {
public:
    void register_component(BaseComponent* component); // Register a new component
    void parse_data(); // Parse data using all registered components
    void print_components(std::ostream &log_stream);
private:
    std::vector<BaseComponent*> components; // List of all registered components
};

#endif // SYSTEMMANAGER_H
