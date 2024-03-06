from django.shortcuts import render
from django.http import HttpResponse

tax_rate=0.15

def index(request):
    return HttpResponse("<h1>this is a site to calculate tax")

def calculate_total_price(request, num):
    total_price = num+(num*tax_rate)
    return HttpResponse(f"<h1>Total price: {total_price}</h1>")

def tax_rate_view(request):
    return HttpResponse(f'tax is {tax_rate}' )

# Create your views here.

