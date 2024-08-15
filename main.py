import uvozi
import os
import preberi
import napisi_csv

spletna_stran = 'https://www.geograf.in/en/table.php?col1=state&col2=continent&col3=area&col4=population&col5=gdp&col6=life&col7=government&col8=density&col9=religion&filter=0&order_by=state&ascdesc=ASC'
mapa = 'države_podatki'
html_ime = 'države.html'
csv_ime = "drzave.csv"

def main(redownload=True, reparse=True):
    path = os.path.join(mapa, html_ime)
    if redownload or not os.path.exists(path):
        uvozi.save_frontpage(spletna_stran, mapa, html_ime)
    else:
        print(f"datoteka {html_ime} že obstaja")

    path = os.path.join(mapa, csv_ime)
    if reparse or not os.path.exists(path):
        drzave = preberi.drzave_from_file(html_ime, mapa)
        napisi_csv.write_drzave_to_csv(drzave, mapa, csv_ime)
    else:
        print("Datoteka csv že obstaja")

if __name__ == '__main__':
    main(False, True)