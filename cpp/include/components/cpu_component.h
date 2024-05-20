#ifndef CPU_COMPONENT_H
#define CPU_COMPONENT_H

#include "base_component.h"

#include <unordered_map>
#include <string>

struct CPUUsage {
    long user;
    long nice;
    long system;
    long idle;
    long iowait;
    long irq;
    long softirq;
    long steal;
};

struct CPUEnergy {
    long long energy_uj;
};

class CPUComponent : public BaseComponent {
public:
    void parse_data() override;
    void print_component(std::ostream &stream) override;

private:
    void parse_cpu_usage();
    void parse_cpu_energy();
    std::unordered_map<std::string, CPUUsage> cpu_usages;
    std::unordered_map<std::string, CPUEnergy> cpu_energy;
};

#endif // CPU_COMPONENT_H
