#include "SystemManager.h"

void SystemManager::registerComponent(BaseComponent* component) {
    components.push_back(component);  // Add the new component to the list of registered components
}

void SystemManager::parseData() {
    for (auto component : components) {
        component->parseData();  // Call the parseData method for each registered component
    }
}