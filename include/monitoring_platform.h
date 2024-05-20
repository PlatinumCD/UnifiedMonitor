#ifndef MONITORINGPLATFORM_H
#define MONITORINGPLATFORM_H

#include <string>
#include <iostream>
#include <fstream>

#include "system_manager.h"
#include "application_manager.h"

class MonitoringPlatform {
public:
    MonitoringPlatform();
    MonitoringPlatform(std::string log_file_name);
    ~MonitoringPlatform();  // Destructor to close the log file if it is open

    void register_system_component(BaseComponent* component); // Register a system component
    void register_application_component(BaseComponent* component); // Register an application component
    void parse_system_data(); // Parse all system data
    void parse_application_data(); // Parse all application data
    void print_data(); // Print system and application data

private:
    std::string log_file_name;
    SystemManager system_manager; // Manage system components
    ApplicationManager application_manager; // Manage application components
    std::ostream* log_stream;  // Stream to either cout or log file
    std::ofstream log_file;  // File stream for logging to a file
};

#endif // MONITORINGPLATFORM_H
