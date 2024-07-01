import re
import os
import funkcije

def read_file_to_string(directory, filename):
    path = os.path.join(directory, filename)
    with open(path, encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def page_to_drzava(page_content):
    return re.findall(r'<tr class="white-bg">(.*?)</tr>', page_content, flags = re.DOTALL)

def get_dict_from_drzava_block(block):
    vzorec_podatki = r"<td>.*?</td><td><a .*?>(.*?)</a></td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>"
    podatki = re.search(vzorec_podatki, block)
    ime = podatki.group(1)
    co2 = funkcije.popravi_stevilke(podatki.group(2))
    obmocje = funkcije.popravi_stevilke(podatki.group(3))
    populacija = funkcije.popravi_stevilke(podatki.group(4))
    gdp = funkcije.popravi_stevilke(podatki.group(5))
    ziv_doba = funkcije.popravi_stevilke(podatki.group(6))
    vlada = podatki.group(7)
    gostota = funkcije.popravi_stevilke(podatki.group(8))
    vera = podatki.group(9)
    return {"ime": ime, "co2": co2, "območje": obmocje, "populacija": populacija, "gdp": gdp, "življenska doba": ziv_doba, "vlada": vlada, "gostota": gostota, "vera": vera}
    
def drzave_from_file(filename, directory):
    page_content = read_file_to_string(directory, filename)
    blocks = page_to_drzava(page_content)
    drzave = [get_dict_from_drzava_block(block) for block in blocks]
    return drzave