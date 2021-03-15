import re
import requests

from bs4 import BeautifulSoup
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .models import Website
from .serializers import WebsiteCreateSerializer, WebsiteSerializer

class WordCountViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin):
    """
    Word count viewset
    Count the frequency of a given word and website
    """
    queryset = Website.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return WebsiteCreateSerializer
        return WebsiteSerializer

    def create(self, request, *args, **kwargs):
        """
        Count the frequency of a given word and website
        Afterwards, save the details in the database
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        url = request.data['url']
        word = request.data['word']
        try:
            count = self.get_word_frequency(url, word)
            self.save_details(word, url, count)
            return Response({'count': count}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def save_details(self, word, url, count):
        """
        Save website details in the database
        """
        website = Website(word=word, url=url, count=count)
        return website.save()

    def get_word_frequency(self, url, word):
        """
        Count the frequency of a given word and website
        """
        boundary = r'\b'
        count = 0
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        search_word = boundary + word + boundary
        text = soup.findAll(text=re.compile(search_word, re.IGNORECASE))

        for t in text:
            text_line = re.findall(search_word, t, re.IGNORECASE)
            count += len(text_line)

        return count
