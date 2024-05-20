#include <string>
#include <iostream>
#include <fstream>

#include "monitoring_platform.h"
#include "system_manager.h"
#include "application_manager.h"

MonitoringPlatform::MonitoringPlatform() : log_stream(&std::cout) {
}

MonitoringPlatform::MonitoringPlatform(std::string log_file_name) : 
	log_file_name(log_file_name) {

	// Create new output method for log file
	log_file.open(log_file_name, std::ios::out | std::ios::trunc); // Open file in write mode and truncate it
	if (log_file.is_open()) {
		log_stream = &log_file;
	} else {
		log_stream = &std::cout;
	}
}

MonitoringPlatform::~MonitoringPlatform() {
	if (log_file.is_open()) {
		log_file.close();
	}
}

void MonitoringPlatform::register_system_component(BaseComponent* component) {
    system_manager.register_component(component);  // Register the system component with the system manager
}

void MonitoringPlatform::register_application_component(BaseComponent* component) {
    application_manager.register_component(component);  // Register the application component with the application manager
}

void MonitoringPlatform::parse_system_data() {
    system_manager.parse_data();  // Parse data for all registered system components
}

void MonitoringPlatform::parse_application_data() {
    application_manager.parse_data();  // Parse data for all registered application components
}

void MonitoringPlatform::print_data() {
    if (log_file.is_open()) {
        log_file.close();
        log_file.open(log_file_name, std::ios::out | std::ios::trunc); // Clear the file contents
        if (!log_file.is_open()) {
            log_stream = &std::cout;
        }
    }
    system_manager.print_components(*log_stream);
}
