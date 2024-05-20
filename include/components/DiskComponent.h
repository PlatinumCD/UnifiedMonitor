#ifndef DISKCOMPONENT_H
#define DISKCOMPONENT_H

#include "BaseComponent.h"

class DiskComponent : public BaseComponent {
public:
    void parseData() override; // Override to provide specific parsing for Disk data
};

#endif // DISKCOMPONENT_H