from unittest import mock

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Website
from .views import WordCountViewSet


class WordCountViewSetTestCase(APITestCase):
    """
    Word count viewset test
    Test the WordCountViewSet
    """

    @mock.patch('app.views.WordCountViewSet.get_word_frequency')
    @mock.patch('app.views.WordCountViewSet.save_details')
    def test_post_create(self, mock_save_details, mock_get_word_frequency):
        """
        Test the POST API endpoint
        """
        count = 1
        mock_get_word_frequency.return_value = count
        mock_save_details.return_value = None
        data = {
            'word': 'test',
            'url': 'https://www.example.com/'
        }
        response = self.client.post(
            '/api/wordcount/',
            data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['count'], count)
        self.assertTrue(mock_get_word_frequency.called)
        self.assertTrue(mock_save_details.called)

    def test_save_details(self):
        """
        Test the save details method
        """
        word = 'test_save'
        url = 'https://www.example.com/'
        count = 1

        word_count_viewset = WordCountViewSet()
        word_count_viewset.save_details(word, url, count)
        response = Website.objects.get(word=word)

        self.assertEqual(response.word, word)
        self.assertEqual(response.url, url)
        self.assertEqual(response.count, count)

    def test_get_word_frequency(self):
        """
        Test the get word frequency method
        """
        word = 'examples'
        url = 'https://www.example.com/'
        count = 1

        word_count_viewset = WordCountViewSet()
        result = word_count_viewset.get_word_frequency(url, word)

        self.assertEqual(result, count)
