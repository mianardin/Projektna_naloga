def popravi_stevilke(niz):
    if "&nbsp;" in niz:
        return niz.replace("&nbsp;", "")
    elif niz == "-- N/A --":
        return 0
    else:
        return niz.replace(',', '.')
    
