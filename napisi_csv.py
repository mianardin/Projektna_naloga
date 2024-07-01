import csv
import os


def write_csv(fieldnames, rows, directory, filename):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, 'w', encoding='utf-8', newline = "") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return


def write_drzave_to_csv(drzave, directory, filename):
    assert drzave and (all(j.keys() == drzave[0].keys() for j in drzave))
    fieldnames = list(drzave[0].keys())
    write_csv(fieldnames, drzave, directory, filename)
