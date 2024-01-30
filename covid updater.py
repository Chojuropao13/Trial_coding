import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://health.detik.com/berita-detikhealth/d-7148398/lagi-studi-baru-bawa-kabar-nggak-enak-buat-yang-pernah-kena-covid"
response = requests.get(url)

html_content = response.content
# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Print the headlines
print(response)