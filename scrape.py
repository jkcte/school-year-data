import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = 'https://www.tomtom.com/traffic-index/manila-traffic/'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 4: Extract all headings
    headings = soup.find_all('h1')
    for heading in headings:
        print("Heading:", heading.text)

    # Step 5: Extract all paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print("Paragraph:", paragraph.text)

    # Step 6: Extract specific elements by class or ID
    # Example: Extract elements with class 'traffic-data'
    traffic_data_elements = soup.find_all(class_='traffic-data')
    for element in traffic_data_elements:
        print("Traffic Data:", element.text)

    # Step 7: Store the data (example: print to console)
    # You can also save to a file or database
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")