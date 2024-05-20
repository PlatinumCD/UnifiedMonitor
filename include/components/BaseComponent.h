#ifndef BASECOMPONENT_H
#define BASECOMPONENT_H

class BaseComponent {
public:
    virtual void parseData() = 0; // Pure virtual method for parsing data
    virtual ~BaseComponent() {} // Virtual destructor for proper cleanup
};

#endif // BASECOMPONENT_H