headers = { 'X-Finnhub-Token' : 'brv97snrh5r9k3fgt6b0'}
import requests

r = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL',headers=headers)
for i in r:
    if i == 'c':
        print (i)

print("Using Json", r.json())