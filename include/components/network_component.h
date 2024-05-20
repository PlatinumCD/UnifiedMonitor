#ifndef NETWORKCOMPONENT_H
#define NETWORKCOMPONENT_H

#include "base_component.h"

class NetworkComponent : public BaseComponent {
public:
    void parse_data() override; // Override to provide specific parsing for Network data
    void print_component(std::ostream &stream) override;
};

#endif // NETWORKCOMPONENT_H
