from django.shortcuts import render, redirect
import request

# Create your views here.

def main(req):
    return render(req, 'main/container.html')

def get_stats(req):
    if req.method == 'GET':
        return render(req,'main/__stats__.html')






def getChartData(req):
    ticker = req.POST['ticker']
    graph_range = req.POST['graph_range']
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart"
    querystring = {f"interval":"5m","region":"US","symbol":"{ticker}","lang":"en","range":"{graph_range}"}
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
    response = getChartData(req.POST['ticker'].upper()).json()
    return render(req, 'main/graph.html', response)
