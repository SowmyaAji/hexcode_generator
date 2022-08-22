import requests
from bs4 import BeautifulSoup

def get_common_codes():
    url='https://en.wikipedia.org/wiki/Hexspeak'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.findAll("table", {"class": "wikitable"})
    codes = ["0xDEADCELL","0xFEEDBULL", "0x1337F001", "0xF00DBEEF", "0x1337BABE"]
    for table in tables:
        body = table.find("tbody")
        rows = body.find_all("tr")
        for row in rows[1:]:
            code = row.find_all("td")[0]
            codes.append(code.find(text=True).strip())
  
    return codes
            

# get_common_codes()