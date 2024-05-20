class ApplicationManager:
    def __init__(self):
        self.components = []

    def register_component(self, component):
        self.components.append(component)

    def parse_data(self):
        for component in self.components:
            component.parse_data()