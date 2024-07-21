import argparse

class CLI:
    def __init__(self, argv):
        self.argv = argv
        self.config_file_path = "config.json"

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Link Aggregation Program")
        parser.add_argument("-c", "--config", help="Path to the configuration file", default="config.json")
        args = parser.parse_args(self.argv)
        self.config_file_path = args.config
        return True

    def get_config_file_path(self):
        return self.config_file_path
