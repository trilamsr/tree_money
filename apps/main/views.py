from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request, 'html/MASTER.html')
