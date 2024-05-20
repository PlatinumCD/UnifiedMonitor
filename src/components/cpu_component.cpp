#include "cpu_component.h"
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <filesystem>

// Function prototypes
std::vector<std::string> split(const std::string& s, char delimiter);
std::string read_file(const std::string& file_path);

// Function to read file content
std::string read_file(const std::string& file_path) {
    std::ifstream file(file_path);
    if (!file.is_open()) {
        return "";
    }
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

void CPUComponent::parse_data() {
    parse_cpu_usage();
    parse_cpu_energy();
}

std::vector<std::string> split(const std::string& s, char delimiter) {
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

void CPUComponent::parse_cpu_usage() {
    std::ifstream file("/proc/stat");
    std::string line;
    while (std::getline(file, line)) {
        if (line.substr(0, 3) == "cpu") {
            auto tokens = split(line, ' ');
            std::string cpu_label = tokens[0];
            if (cpu_label == "cpu") continue; // Skip the aggregate line
            
            if (tokens.size() < 8) continue; // Sanity check
            
            CPUUsage usage;
            usage.user = std::stol(tokens[1]);
            usage.nice = std::stol(tokens[2]);
            usage.system = std::stol(tokens[3]);
            usage.idle = std::stol(tokens[4]);
            usage.iowait = std::stol(tokens[5]);
            usage.irq = std::stol(tokens[6]);
            usage.softirq = std::stol(tokens[7]);
            usage.steal = (tokens.size() > 8) ? std::stol(tokens[8]) : 0;

            cpu_usages[cpu_label] = usage;
        }
    }
}

void CPUComponent::parse_cpu_energy() {
    std::string rapl_base_path = "/sys/class/powercap/intel-rapl";
    for (const auto& entry : std::filesystem::directory_iterator(rapl_base_path)) {
        if (entry.is_directory() && entry.path().filename().string().find("intel-rapl:") == 0) {
            std::string energy_file_path = entry.path().string() + "/energy_uj";
            std::string energy_str = read_file(energy_file_path);
            if (!energy_str.empty()) {
                try {
		    CPUEnergy energy;
                    long long energy_uj = std::stoll(energy_str);
                    energy.energy_uj = energy_uj;
		    cpu_energy[entry.path().filename()] = energy;
                } catch (const std::exception& e) {
                    std::cerr << "Error parsing energy usage from " << entry.path().filename() << ": " << e.what() << std::endl;
                }
            }
        }
    }
}

void CPUComponent::print_component(std::ostream &stream) {
    stream << "CPU Usage:" << std::endl;
    for (const auto& cpu : cpu_usages) {
        stream << cpu.first << ":" << std::endl;
        stream << "  user: " << cpu.second.user << std::endl;
        stream << "  nice: " << cpu.second.nice << std::endl;
        stream << "  system: " << cpu.second.system << std::endl;
        stream << "  idle: " << cpu.second.idle << std::endl;
        stream << "  iowait: " << cpu.second.iowait << std::endl;
        stream << "  irq: " << cpu.second.irq << std::endl;
        stream << "  softirq: " << cpu.second.softirq << std::endl;
        stream << "  steal: " << cpu.second.steal << std::endl;
    }

    stream << "CPU Energy Consumption (μJ):" << std::endl;
    for (const auto& energy_entry : cpu_energy) {
        stream << "  " << energy_entry.first << ": " << energy_entry.second.energy_uj << " μJ" << std::endl;
    }
}
