import json

class Config:
    def __init__(self, network_interfaces):
        self.network_interfaces = network_interfaces

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return Config(data["networkInterfaces"])
