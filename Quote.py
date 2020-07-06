from Equations import *
headers = { 'X-Finnhub-Token' : 'brv97snrh5r9k3fgt6b0'} #API
import requests
import json


inp = input('Please input a stock Ticker, if you want to quit please press 1 ')

while inp != '1': #Will continue until users enters 1
    ticker = 'https://finnhub.io/api/v1/quote?symbol='+ inp.upper()

    data = requests.get(ticker,headers=headers)
    print('From Data:\n',data.json())

    inp = input('Please input another stock Ticker, if you want to quit please press 1 ')

