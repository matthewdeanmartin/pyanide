"""CLI interface for pyanide"""

import argparse

from pyanide import kill_process_by_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("process_name", help="name of the process to kill")
    parser.add_argument("-i", "--interval", type=int, default=60, help="interval to check if the process has come back")
    args = parser.parse_args()

    process_name = args.process_name
    interval = args.interval

    kill_process_by_name(process_name, interval)
