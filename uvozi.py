import os
import requests

spletna_stran = 'https://www.geograf.in/en/table.php?col1=state&col2=continent&col3=area&col4=population&col5=gdp&col6=life&col7=government&col8=density&col9=religion&filter=0&order_by=state&ascdesc=ASC'

mapa = 'države_podatki'

html_ime = 'države.html'

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