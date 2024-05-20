#ifndef MEMORYCOMPONENT_H
#define MEMORYCOMPONENT_H

#include "base_component.h"

class MemoryComponent : public BaseComponent {
public:
    void parse_data() override; // Override to provide specific parsing for Memory data
    void print_component(std::ostream &stream) override;
};

#endif // MEMORYCOMPONENT_H
