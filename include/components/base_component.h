#ifndef BASECOMPONENT_H
#define BASECOMPONENT_H

#include <iostream>

class BaseComponent {
public:
    virtual void parse_data() = 0; // Pure virtual method for parsing data
    virtual void print_component(std::ostream &stream) = 0; // Pure virtual method for printing component data
    virtual ~BaseComponent() {} // Virtual destructor for proper cleanup
};

#endif // BASECOMPONENT_H
