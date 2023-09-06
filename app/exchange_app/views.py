from django.shortcuts import render
import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def exchange(request):
    response = requests.get(url=f"http://api.exchangeratesapi.io/v1/latest?access_key={os.getenv('API_TOKEN')}").json()
    currencies = response.get('rates')

    if request.method == 'GET':
        context = {
            'currencies': currencies
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)

    if request.method == 'POST':
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'currencies': currencies,
            'converted_amount': converted_amount,
        }

        return render(request=request, template_name='exchange_app/index.html', context=context)
