import sys
import threading
import json
from config import Config
from network_interface import NetworkInterface
from link_aggregation import LinkAggregation
from cli import CLI

def start_link_aggregation(link_agg):
    try:
        if not link_agg.initialize():
            print("Error initializing link aggregation")
            return

        link_agg.start()
        input("Link aggregation started. Press Enter to stop...\n")
        link_agg.stop()
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    try:
        # Parse command-line arguments
        cli = CLI(sys.argv[1:])
        if not cli.parse_arguments():
            return 1  # Exit if arguments are not parsed successfully

        # Load configuration
        config = Config.load_from_file(cli.get_config_file_path())

        # Initialize network interfaces
        interfaces = []
        for iface_name in config.network_interfaces:
            try:
                iface = NetworkInterface(iface_name)
                iface.initialize()
                interfaces.append(iface)
            except Exception as e:
                print(f"Error initializing interface {iface_name}: {e}")
                return 1

        # Initialize link aggregation
        link_agg = LinkAggregation(interfaces)

        # Start link aggregation in a separate thread
        link_agg_thread = threading.Thread(target=start_link_aggregation, args=(link_agg,))
        link_agg_thread.start()
        link_agg_thread.join()  # Wait for the thread to finish

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
