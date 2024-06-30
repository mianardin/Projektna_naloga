import uvozi
import os

mapa = uvozi.mapa
html = uvozi.html_ime
url = uvozi.spletna_stran


def main(redownload=True, reparse=True):
    path = os.path.join(mapa, html)
    if redownload or not os.path.exists(path):
        uvozi.save_frontpage(url, mapa, html)
    else:
        print(f"datoteka {html} že obstaja")

    #path = os.path.join(drivers_directory, csv_filename)
    #if reparse or not os.path.exists(path):
        #drivers = izlusci.drivers_from_file(frontpage_filename, drivers_directory)
        #write_csv.write_drivers_to_csv(drivers, drivers_directory, csv_filename)
    #else:
        #print("Datoteka csv že obstaja")


if __name__ == '__main__':
    main(False, True)