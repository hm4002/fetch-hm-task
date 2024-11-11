# HTTP Endpoint Health Check Tool
## Overview
This Python program checks the health of a set of HTTP endpoints provided in a YAML configuration file. It sends requests every 15 seconds, determines the status of each endpoint, and logs the availability percentage of each domain over time.

## Features
Parses a YAML configuration file containing HTTP endpoints.
Sends requests at 15-second intervals.
Checks if the response status is within the 200–299 range and if the response latency is below 500 ms to determine if an endpoint is "UP".
Logs the cumulative availability percentage of each domain after every test cycle.
## Prerequisites
Ensure you have Python 3 installed along with the required libraries:

- requests
- PyYAML
Install them using:

`pip install requests pyyaml`

## How to Use
1. Clone or download the repository containing this script.
2. Prepare a YAML configuration file like the one provided in this repo named "input.yaml".
3. Run the script using the following command:
`python healthcheck.py`
4. Enter the path to the YAML configuration file when prompted.

Thank you for taking your time to review. :)