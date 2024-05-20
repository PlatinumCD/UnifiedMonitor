#ifndef CPUCOMPONENT_H
#define CPUCOMPONENT_H

#include "BaseComponent.h"

class CPUComponent : public BaseComponent {
public:
    void parseData() override; // Override to provide specific parsing for CPU data
};

#endif // CPUCOMPONENT_H