def popravi_stevilke(niz):
    if "&nbsp;" in niz:
        return niz.replace("&nbsp;", "")
    elif niz == "-- N/A --":
        return 0
    else:
        return niz.replace(',', '.')
    
def popravi_ime(niz):
    if "," in niz:
        deli = niz.split(", ")
        return deli[1] + " " + deli[0]
    else:
        return niz