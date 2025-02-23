from pprint import pprint

from bs4 import BeautifulSoup
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import datetime, timedelta


@api_view(['GET'])
def get_currency_data(request):
    # Get Bitcoin price in EUR
    bitcoin_response = requests.get('https://blockchain.info/tobtc?currency=EUR&value=1')
    bitcoin_eur = 1 / float(bitcoin_response.text)

    # Get EUR to GBP rate from ECB
    ecb_response = requests.get('https://data.ecb.europa.eu/main-figures/ecb-interest-rates-and-exchange-rates/exchange-rates')
    soup = BeautifulSoup(ecb_response.text, 'html.parser')
    rate_element = soup.find(name='div', attrs={'data-card-detail-url': '/data/datasets/EXR/EXR.M.GBP.EUR.SP00.A'})
    rate_value = rate_element.find('p', class_='flex chart-ratio').find('span').text.strip()
    eur_to_gbp = float(rate_value)

    # Calculate Bitcoin price in GBP
    bitcoin_gbp = bitcoin_eur * eur_to_gbp

    return Response({
        'bitcoin_eur': bitcoin_eur,
        'eur_to_gbp': eur_to_gbp,
        'bitcoin_gbp': bitcoin_gbp
    })
