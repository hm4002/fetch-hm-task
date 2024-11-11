import time
import requests
import yaml
from urllib.parse import urlparse

# Function to load and parse the YAML file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to send HTTP requests and evaluate the response
def check_endpoint(endpoint):
    method = endpoint.get('method', 'GET').upper()
    url = endpoint['url']
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    try:
        start_time = time.time()
        response = requests.request(method, url, headers=headers, data=body, timeout=5)
        latency = (time.time() - start_time) * 1000  # Convert to ms
        if 200 <= response.status_code < 300 and latency < 500:
            return True
    except requests.exceptions.RequestException:
        pass

    return False

# Main function to run the health check
def run_health_check(config_path):
    config = load_config(config_path)
    domain_stats = {}

    while True:
        for endpoint in config:
            domain = urlparse(endpoint['url']).netloc
            if domain not in domain_stats:
                domain_stats[domain] = {'up_count': 0, 'total_count': 0}

            is_up = check_endpoint(endpoint)
            domain_stats[domain]['total_count'] += 1
            if is_up:
                domain_stats[domain]['up_count'] += 1

        # Log results
        for domain, stats in domain_stats.items():
            availability = (stats['up_count'] / stats['total_count']) * 100
            print(f"{domain} has {round(availability)}% availability")

        time.sleep(15)

if __name__ == "__main__":
    config_file_path = input("Enter the path to the YAML config file: ").strip()
    run_health_check(config_file_path)
