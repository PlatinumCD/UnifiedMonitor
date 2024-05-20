#include "application_manager.h"

void ApplicationManager::register_component(BaseComponent* component) {
    components.push_back(component);  // Add the new component to the list of registered components
}

void ApplicationManager::parse_data() {
    for (auto component : components) {
        component->parse_data();  // Call the parse_data method for each registered component
    }
}