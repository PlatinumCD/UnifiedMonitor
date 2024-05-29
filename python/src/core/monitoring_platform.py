import os
import sys

from core.system_manager import SystemManager
from core.application_manager import ApplicationManager

class MonitoringPlatform:
    def __init__(self, log_file_name=None):
        self.log_file_name = log_file_name
        self.system_manager = SystemManager()
        self.application_manager = ApplicationManager()

        if log_file_name:
            self.log_file = open(log_file_name, 'w', buffering=1)  # Open once, line-buffered
            self.log_stream = self.log_file
        else:
            self.log_stream = sys.stdout

    def __del__(self):
        self.close_log_file()

    def close_log_file(self):
        if hasattr(self, 'log_file') and self.log_file and not self.log_file.closed:
            self.log_file.close()

    def register_system_component(self, component):
        self.system_manager.register_component(component)

    def register_application_component(self, component):
        self.application_manager.register_component(component)

    def parse_system_data(self):
        self.system_manager.parse_data()

    def parse_application_data(self):
        self.application_manager.parse_data()

    def print_data(self):
        if self.log_file:
            self.log_file.seek(0)  # Move cursor to the beginning of the file
#            self.log_file.truncate()  # Truncate the file (delete all content)
        self.system_manager.print_components(self.log_stream)
        if self.log_file:
            self.log_file.flush()
