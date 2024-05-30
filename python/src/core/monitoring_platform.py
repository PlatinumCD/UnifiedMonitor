import os
import sys
import csv

from core.system_manager import SystemManager
from core.application_manager import ApplicationManager

class MonitoringPlatform:
    def __init__(self, stream_file_name=None, record_file_name=None):
        self.stream_file_name = stream_file_name
        self.record_file_name = record_file_name
        self.system_manager = SystemManager()
        self.application_manager = ApplicationManager()

        if stream_file_name:
            self.stream_file = open(stream_file_name, 'w', buffering=1)  # Open once, line-buffered
            self.stream = self.stream_file
        else:
            self.stream_file = None
            self.stream = None
            
        if record_file_name:
            self.record_file = open(record_file_name, 'w')  # Open CSV file for writing
            self.csv_writer = csv.writer(self.record_file)
        else:
            self.record_file = None
            self.csv_writer = None

        if not stream_file_name and not record_file_name:
            self.stream = sys.stdout

    def __del__(self):
        self.close_stream_file()
        self.close_record_file()

    def close_stream_file(self):
        if hasattr(self, 'stream_file') and self.stream_file and not self.stream_file.closed:
            self.stream_file.close()

    def close_record_file(self):
        if hasattr(self, 'record_file') and self.record_file and not self.record_file.closed:
            self.record_file.close()

    def register_system_component(self, component):
        self.system_manager.register_component(component)

    def register_application_component(self, component):
        self.application_manager.register_component(component)

    def parse_system_data(self):
        self.system_manager.parse_data()

    def parse_application_data(self):
        self.application_manager.parse_data()

    def print_data(self):
        if not self.stream:
            return
        if self.stream_file:
            self.stream_file.seek(0)
        self.system_manager.print_components(self.stream)
        if self.stream_file:
            self.stream_file.flush()

    def record_data(self):
        if self.csv_writer:
            self.system_manager.record_components(self.csv_writer)
            self.record_file.flush()
