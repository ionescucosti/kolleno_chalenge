from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import URLData
from .serializers import URLDataSerializer
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class URLDataViewSet(viewsets.ModelViewSet):
    queryset = URLData.objects.all()
    serializer_class = URLDataSerializer

    def create(self, request):
        url = request.data.get('url')

        try:
            response = requests.get(url)
            response.raise_for_status()

            parsed_url = urlparse(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            url_data = {
                'url': url,
                'domain_name': parsed_url.netloc,
                'protocol': parsed_url.scheme,
                'title': soup.title.string if soup.title else None,
                'images': [img.get('src') for img in soup.find_all('img')],
                'stylesheets_count': len(soup.find_all('link', rel='stylesheet'))
            }

            serializer = self.get_serializer(data=url_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except requests.exceptions.RequestException:
            return Response(
                {'error': 'Invalid URL or unable to fetch the page'},
                status=status.HTTP_400_BAD_REQUEST
            )
