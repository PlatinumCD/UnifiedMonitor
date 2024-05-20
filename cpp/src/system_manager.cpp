#include <string>

#include "system_manager.h"

void SystemManager::register_component(BaseComponent* component) {
    components.push_back(component);  // Add the new component to the list of registered components
}

void SystemManager::parse_data() {
    for (auto component : components) {
        component->parse_data();  // Call the parse_data method for each registered component
    }
}

void SystemManager::print_components(std::ostream &log_stream) {
    for (auto component : components) {
        component->print_component(log_stream);
    }
}
