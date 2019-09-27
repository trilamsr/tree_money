from django.shortcuts import render, redirect, HttpResponse
import requests
import json
import time

# Create your views here.

def main(req):
    return render(req, 'main/container.html')

def get_stats(req):
    if req.method == 'GET':
        return render(req,'main/__stats__.html')






def getChartData(ticker, graph_range, interval='5m'):
    ticker = ticker
    graph_range = graph_range
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"
    querystring = {"interval":interval,"region":"US","symbol":ticker,"lang":"en","range":graph_range}
    headers = {
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
    'x-rapidapi-key': "9cf6f84669mshf37812fae4d0b86p19dc92jsnac00aa2c3e97"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response

# def getTicker(req):
#     ticker = req.POST['ticker']
#     graph_range = req.POST['graph_range']
#     return redirect(f"/getGraph/{ticker}/{graph_range}")

def getGraph(req):
    response = getChartData(req.POST['ticker'].upper(),req.POST['graph_range'],req.POST['interval']).json()
    print(type(response))
    gettime = response['chart']['result'][0]['timestamp']
    # print(gettime)
    # for i in range(len(gettime)):
    #     gettime[i] = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(gettime[i]))
    #     print(gettime[i])
    # print(gettime)
    context = {
        'symbol': str(req.POST['ticker'].upper()),
        'time': response['chart']['result'][0]['timestamp'],
        'data': response['chart']['result'][0]['indicators']['quote'][0]['open']
    }
    return render(req, 'main/graph.html', context)

    # return HttpResponse(response)
