import os
import requests
from bs4 import BeautifulSoup

# Base URL to scrape and download the dataset
BASE_URL = "http://cicresearch.ca/CICDataset/CIC-IDS-2017/Dataset/CIC-IDS-2017/"
DOWNLOAD_DIR = "data/raw/"  # Destination folder for downloaded files

def download_file(url, dest_path):
    """Download a file from the given URL and save it locally."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {dest_path}")
    else:
        print(f"Failed to download: {url}")

def download_dataset():
    """Scrape the dataset directory and download the files."""
    response = requests.get(BASE_URL)
    if response.status_code != 200:
        print("Failed to access the URL.")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all file links in the dataset directory
    links = soup.find_all('a')
    
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)  # Ensure output folder exists

    for link in links:
        href = link.get('href')
        if href.endswith(".csv") or href.endswith(".zip"):  # Download CSV or ZIP files only
            file_url = BASE_URL + href
            dest_file_path = os.path.join(DOWNLOAD_DIR, href)
            download_file(file_url, dest_file_path)

if __name__ == "__main__":
    download_dataset()