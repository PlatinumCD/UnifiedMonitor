#ifndef MEMORYCOMPONENT_H
#define MEMORYCOMPONENT_H

#include "BaseComponent.h"

class MemoryComponent : public BaseComponent {
public:
    void parseData() override; // Override to provide specific parsing for Memory data
};

#endif // MEMORYCOMPONENT_H