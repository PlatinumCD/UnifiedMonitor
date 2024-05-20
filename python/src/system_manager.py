class SystemManager:
    def __init__(self):
        self.components = []

    def register_component(self, component):
        self.components.append(component)

    def parse_data(self):
        for component in self.components:
            component.parse_data()

    def print_components(self, log_stream):
        for component in self.components:
            component.print_component(log_stream)
