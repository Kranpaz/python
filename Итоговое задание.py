import socket
import sys
import urllib.request
import json
import urllib
from flask import Flask
app = Flask(__name__)
import requests

class Url:
    def __init__(self, url, ip):
        self.url = url
        self.ip = ip
    def exist(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.ip = socket.gethostbyname(ad)
                print(f'Ваш сайт {self.url} найден, его IP-адрес: {self.ip}.')


        except:
            print(f'Ваш сайт {self.url} не найден.')
            sys.exit()

class Info_url:
    def __init__(self, url, ip, region, city, loc):
        self.url = url
        self.ip = ip
        self.region = region
        self.city = city
        self.loc = loc

    def opr(self):
        with urllib.request.urlopen(f"https://ipinfo.io/{address.ip}/json") as ur:
            data = json.load(ur)
        self.region = data['region']
        self.city = data['city']
        self.loc = data['loc']

    def js(self):
        return (f'Информация о сайте \n'
                f'url: {self.url}; \n'
                f'ip: {self.ip}; \n'
                f'region: {self.region}; \n'
                f'city: {self.city}; \n'
                f'loc: {self.loc}.')

@app.route('/')
def vivod():
    return g

if __name__ == '__main__':
    ad = input("Введите адрес сайта: https://")
    a = 'https://' + ad
    address = Url(a, '')
    address.exist()
    inf = Info_url(address.url, address.ip, '', '', '')
    inf.opr()
    g = inf.js()
    print('\n' + g + '\n')
    app.run()