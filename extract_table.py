import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.w3schools.com/html/html_tables.asp'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')


tables = soup.find_all('table')
table = tables[0]  


headers = [th.get_text(strip=True) for th in table.find_all('th')]


rows = []
for tr in table.find_all('tr')[1:]:
    cells = tr.find_all(['td', 'th'])
    row = [cell.get_text(strip=True) for cell in cells]
    if row:
        rows.append(row)


with open('sample_table.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if headers:
        writer.writerow(headers)
    writer.writerows(rows)

print("✅The table has been saved in 'sample_table.csv'")
