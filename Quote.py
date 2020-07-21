from Equations import *
import config
import requests
import json
#headers = { 'X-Finnhub-Token' : 'brv97snrh5r9k3fgt6b0'} #API

headers = { config.access_token : config.api_key}

inp = input('Please input a stock Ticker, if you want to quit please press 1 ')

while inp != '1': #Will continue until users enters 1
    ticker = 'https://finnhub.io/api/v1/quote?symbol='+ inp.upper()#quote
    profile = 'https://finnhub.io/api/v1/stock/profile2?symbol=' + inp.upper()#General information about company

    quote = requests.get(ticker,headers=headers)
    quote = quote.json()#information
    profile = requests.get(profile,headers=headers)
    profile = profile.json()#gets information
    print('The quote for the stock: ',inp.upper(), ' is below')
    for x in quote: #Loops through the information
        print(x, ':',quote[x])
    print('Below is the company general information')
    for x in profile: #Loop through profile
        print(x,':',profile[x])

    print("If you would like the Company news please input yes and a 'From Date' and also a 'To date', if not please input no") 
    choice = input("Choice: ")
    if choice.upper() == "YES":
        From = input("Please input a From date in the form of 'Year-Month-Day' ")
        From = '&from=' + From
        to = input("Please input a 'To' in the same format ")
        to = '&to='+to
        news = 'https://finnhub.io/api/v1/company-news?symbol=' +inp.upper() + From + to
        test = requests.get(news,headers=headers)
        test = test.json()
        for dic in test:
            for key in dic:
                print(key, ':',dic[key])
    inp = input('Please input another stock Ticker, if you want to quit please press 1 ')

