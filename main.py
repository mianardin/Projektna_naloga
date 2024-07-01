import uvozi
import os
import preberi
import napisi_csv

mapa = uvozi.mapa
html = uvozi.html_ime
url = uvozi.spletna_stran
csv_ime = "drzave.csv"


def main(redownload=True, reparse=True):
    path = os.path.join(mapa, html)
    if redownload or not os.path.exists(path):
        uvozi.save_frontpage(url, mapa, html)
    else:
        print(f"datoteka {html} že obstaja")

    path = os.path.join(mapa, csv_ime)
    if reparse or not os.path.exists(path):
        drzave = preberi.drzave_from_file(html, mapa)
        napisi_csv.write_drzave_to_csv(drzave, mapa, csv_ime)
    else:
        print("Datoteka csv že obstaja")

if __name__ == '__main__':
    main(False, True)