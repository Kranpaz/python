from LxmlSoup import LxmlSoup
import requests

html = requests.get("https://nsk.sunlight.net/catalog/").text
#print(html)

soup = LxmlSoup(html)   # создаём экземпляр класса LxmlSoup
links = soup.find_all('a', class_='cl-item-link js-cl-item-link js-cl-item-root-link')  # получаем список ссылок и наименований
for i, link in enumerate(links):
    url = link.get("href")  # получаем ссылку на товар
    name = link.text()      # извлекаем наименование из блока со ссылкой
    price = soup.find_all("div", class_="cl-item-info-price-discount")[i].text()    # извлекаем цену
    print(i)
    print(f"Url - {url}")
    print(f"Name - {name}")
    print(f"Price - {price}")