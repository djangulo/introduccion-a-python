import sys
import requests
import bs4

URL = 'https://es.wikipedia.org/wiki/Anexo:Comparaci%C3%B3n_de_procesadores_Intel'

def get_table():
    res = requests.get(URL)
    soup = bs4.BeautifulSoup(res.text, features="html5lib")

table = soup.select("table")
    headers = table[1].select("th")
    data = table[1].select("td")

    return headers, data


def filter_columns(headers, data, want=[]):
    idx = []
    for w in want:
        for h in headers:
            if w.lower() in h.getText().lower():
                idx.append(headers.index(h))
    new_headers = []
    for i in idx:
        new_headers.append(headers[i].getText())

    new_data = []
    for k in range(0, len(data), len(headers)):
        d = []
        for i in idx:
            d.append(data[k + i].getText())
        new_data.append(d)

    for k in range(10):

    return new_headers, new_data

if __name__ == "__main__":
    headers, data = get_table()
    headers, data = filter_columns(headers, data, ["procesador", "nombre del código", "frecuencia"])
    for h in headers:
        sys.stdout.write("{}\t".format(h))
    sys.stdout.write("\n")
    for d in data:
        sys.stdout.write("{}\t{}\t{}\n".format(*d))
