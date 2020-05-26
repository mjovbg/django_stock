from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
# Create your views here.

# create function for home page
def home(request):
    # request is the browser request that users make
    import requests
    import json
    # you need requests and json to make the request

    # for search form - pay attention to name in base.html - ticker - this is how to make a reference
    if request.method == 'POST':
        ticker = request.POST['ticker']     # name of the form's input field in base html.
        # create api request:
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_905361298c714746ad5a53e7e33b4335")
        try:
            # parse api result using json
            api = json.loads(api_request).content
        except Exception as e:
            api = "Error...."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter ticker above"})

def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json
    if request.method == 'POST':
        # now dealing the forms django way:
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('stock has been added'))
            return redirect ('add_stock')
    else:
    # pulling from db:
        ticker = Stock.objects.all()
        output = []     # list for ticekr_item
        for ticker_item in ticker:
            # with the for loop you make api calls (as many as there are stocks)
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_905361298c714746ad5a53e7e33b4335")
            try:
                # parse api result using json
                api = json.loads(api_request).content
                output.append(api)      # adding api output to the list. after you pass it in the context variable
            except Exception as e:
                api = "Error...."

    # passing the context variable {}
        return render(request, 'add_stock.html', {'ticker': ticker, 'output':output})

def delete (request, stock_id):
    # get the stock with particular id number
    item = Stock.objects.get(pk=stock_id)
    # deleting item:
    item.delete()
    messages.success(request, ('Stock Deleted!'))
    return redirect('delete_stock')

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'tikcer': ticker})




