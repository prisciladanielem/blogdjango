from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

class HomeViewTest(TestCase):

    def test_home_status_code(self):
        client = Client() #É um navegador próprio do django para executar os testes.
        response = client.get(reverse('home')) #Tenta acessar a url home e captura a resposta
        self.assertEquals(response.status_code, 200) #verifica se o response foi igual a 200
