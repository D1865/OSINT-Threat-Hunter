import argparse
import requests
from bs4 import BeautifulSoup
import json

def collect_from_source_1():
    # Example: Collecting data from a security bulletin
    url = "http://example-security-bulletin.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Process and extract relevant data
    data = []
    for item in soup.find_all('div', class_='bulletin'):
        title = item.find('h2').text
        link = item.find('a')['href']
        data.append({'title': title, 'link': link})
    return data

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="OSINT Collector for Threat Hunting")
    parser.add_argument('--output', type=str, default='osint_data.json', help="Output file for the collected data.")
    args = parser.parse_args()

    collected_data = collect_from_source_1()
    save_data(collected_data, args.output)
    print(f"Data collected and saved to {args.output}")

if __name__ == "__main__":
    main()
