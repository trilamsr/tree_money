from django.shortcuts import render, redirect, HttpResponse
import requests
from newsapi import NewsApiClient

# Create your views here.

def main(req):
    return render(req, 'main/container.html')

def get_data_stats(ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"
    querystring = {"region":"US","lang":"en","symbol":ticker}
    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "9cf6f84669mshf37812fae4d0b86p19dc92jsnac00aa2c3e97"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response


# cannot mix country/category param with sources param.
def get_news(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        newsapi = NewsApiClient(api_key='186be768b0384fa986e05bb437408536')
        all_articles = newsapi.get_everything(q=ticker,language='en',page=2)
        return render(request, 'main/__news__.html', {'headlines': all_articles})


def get_nav(request):
    if request.method == 'POST':
        ticker = request.POST['ticker']
        return render(request, 'main/__nav_bar__.html', {'ticker': ticker})


def get_data(str):
    print(str)
    def get(req):
        if req.method == 'POST':
            print('-------inside POST-----')
            response = get_data_stats(req.POST['ticker'].upper()).json()
            return render(req,f'main/__{str}__.html', response)
    return get
