#ifndef NETWORKCOMPONENT_H
#define NETWORKCOMPONENT_H

#include "BaseComponent.h"

class NetworkComponent : public BaseComponent {
public:
    void parseData() override; // Override to provide specific parsing for Network data
};

#endif // NETWORKCOMPONENT_H