class NetworkInterface:
    def __init__(self, name):
        self.name = name

    def initialize(self):
        # Platform-specific code to initialize the network interface
        # For example, on Windows, you might use pyPcap or a similar library
        # If initialization fails, raise an exception
        if False:  # Replace with actual initialization check
            raise RuntimeError(f"Failed to initialize network interface: {self.name}")
