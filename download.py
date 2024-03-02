from src.download_webpage import *
import os

# Path to the file containing URLs
links_file_path = 'web_links.txt'

# Directory where you want to save the webpages
download_folder = 'example/'  # Specify your own path

# Ensure the download folder exists
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Read URLs from the file and download each webpage
with open(links_file_path, 'r') as file:
    for url in file.readlines():
        url = url.strip()  # Remove any leading/trailing whitespace characters
        if url:  # Check if the URL is not empty
            print(f"Downloading: {url}")
            try:
                download_webpage(url, download_folder)
                print(f"Successfully downloaded {url}")
            except Exception as e:
                print(f"Failed to download {url}. Error: {e}")

print("All webpages downloaded successfully.")