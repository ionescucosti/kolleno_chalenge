# Kolleno Challenge API

A Django REST API that provides URL analysis and currency conversion services.

## Features

### Part One: URL Analysis
- Validates and analyzes URLs
- Extracts domain name, protocol, title, images and stylesheet count
- Provides CRUD operations for URL analysis data
- Stores results in database

### Part Two: Currency Data
- Bitcoin price in EUR (15min delayed)
- EUR to GBP conversion rate from ECB
- Bitcoin price in GBP (calculated using ECB rate)

## Setup

1. Create virtual environment:
	python -m venv venv
	source venv/bin/activate

2. Install dependencies:
	pip install -r requirements.txt

3. Run migrations:
	python manage.py makemigrations
	python manage.py migrate

4. Run server:
	python manage.py runserver


## API Endpoints
### URL Analysis
	POST /api/urls/ - Create new URL analysis
	GET /api/urls/ - List all analyzed URLs
	GET /api/urls/{id}/ - Get specific URL analysis
	DELETE /api/urls/{id}/ - Delete URL analysis

### Currency Data
	GET /api/currency-data/ - Get current Bitcoin and EUR/GBP rates

## Technologies
	Python 3.11+
	Django
	Django REST Framework
	BeautifulSoup4
	Requests

## Resources
	ECB API: https://data.ecb.europa.eu/help/api/overview
	Bitcoin API: https://www.blockchain.com/api/exchange_rates_api
