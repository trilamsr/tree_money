from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request, 'main/container.html')


def getTicker(request):
    ticker = request.POST['search_ticker']
    graph_range = '1d'
    return redirect(f"/getGraph/{ticker}/{graph_range}")

def getGraph(request, ticker, graph_range):
    context = {
        'ticker': ticker,
        'graph_range': graph_range
    }
    return 
