#ifndef DISKCOMPONENT_H
#define DISKCOMPONENT_H

#include "base_component.h"

class DiskComponent : public BaseComponent {
public:
    void parse_data() override; // Override to provide specific parsing for Disk data
    void print_component(std::ostream &stream) override;
};

#endif // DISKCOMPONENT_H
