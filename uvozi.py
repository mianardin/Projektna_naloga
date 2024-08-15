import os
import requests

def download_url_to_string(url):
    headers = {"User-Agent": "Chrome/124.0.6367.201"}
    page_content = requests.get(url, headers=headers)
    return page_content.text

def save_string_to_file(text, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(text)
    return None

def save_frontpage(page, directory, filename):
    text = download_url_to_string(page)
    save_string_to_file(text, directory, filename)
    return text