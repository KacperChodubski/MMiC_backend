#!/usr/bin/python3

import subprocess
import argparse

parser = argparse.ArgumentParser(
    prog="Utils",
    description="Utils for docker"
)

parser.add_argument('command')

args = parser.parse_args()

if args.command == "up":
    command = ["docker", "compose", "up", "--build", "-d"]
    subprocess.run(command, check=True)

if args.command == "down":
    command = ["docker", "compose", "down"]
    subprocess.run(command, check=True)

if args.command == "logs":
    command = ["docker", "compose", "logs", "-f"]
    try:
        subprocess.run(command, check=True)
    except:
        pass
