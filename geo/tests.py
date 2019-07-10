# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from unittest import mock
from geo.geo_api import get_address
from geo.models import Geo
from datetime import timedelta

connection = APIClient()
class InvoiceTests(APITestCase):
    def setUp(self):
        self.data = "india"

    @mock.patch('geo.views.get_address')
    def test_calling_address(self, get_address_function):
        get_address_function.return_value = self.data        
        response = connection.get('/geo/get_address/-34.433333/-58.7000', format='json')
        get_address_function.assert_called_with("-34.433333", "-58.7000")
        self.assertEqual(get_address_function.called, True)    

    @mock.patch('geo.views.get_address')
    def test_address_not_calling_second_time(self, get_address_function):
        get_address_function.return_value = self.data        
        response = connection.get('/geo/get_address/-34.433333/-58.7000', format='json')
        self.assertEqual(response.data["name"], self.data)
        response = connection.get('/geo/get_address/-34.433333/-58.7000', format='json')     
        self.assertEqual(get_address_function.call_count, 1)

    @mock.patch('geo.views.get_address')
    def test_address_older_one_day(self, get_address_function):
        get_address_function.return_value = self.data        
        geo = Geo.objects.create(lat="10", lon="10", place="india")
        Geo.objects.filter(id=geo.id).update(date=geo.date-timedelta(days=1))      
        response = connection.get('/geo/get_address/10/10', format='json')
        self.assertEqual(get_address_function.called, True)                             