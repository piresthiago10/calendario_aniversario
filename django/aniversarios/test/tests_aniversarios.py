from django.http import response
from rest_framework.test import APITestCase
from aniversarios.models import Aniversario
from django.urls import reverse
from rest_framework import status


class AlunosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Aniversarios-list')
        self.aniversario_1 = Aniversario.objects.create(
            nome='John Lennon', data_aniversario="09/10/1940"
        )
        self.aniversario_2 = Aniversario.objects.create(
            nome='George Harrison', data_aniversario="25/02/1943"
        )
        self.aniversario_3 = Aniversario.objects.create(
            nome='Paul McCartney', data_aniversario="18/06/1942"
        )
        self.aniversario_4 = Aniversario.objects.create(
            nome='Ringo Starr', data_aniversario="07/07/1940"
        )

    def test_requisicao_get_para_listar_aniversarios(self):
        """ Teste para verificar a requisição GET para listar os aniversários """

        response = self.client.get(self.list_url)
        self.assertAlmostEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_aniversario(self):
        """ Teste para verificar a requisição POST para criar um aniversario """

        data = {
            'nome': 'Billy Preston',
            'data_aniversario': '02/09/1946'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_para_criar_aniversario_nome_alfanumerico(self):
        """ Teste para verificar a requisição POST para criar um aniversario
        com nome do aniversariante com números """

        data = {
            'nome': 'Y0ko 0no',
            'data_aniversario': '18/02/1933'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_post_para_criar_aniversario_ano_errada(self):
        """ Teste para verificar a requisição POST para criar um aniversario utilizando
        uma data de aniversario superior ao ano atual"""

        data = {
            'nome': 'Billy Preston',
            'data_aniversario': '02/09/3000'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_post_para_criar_aniversario_data_errada(self):
        """ Teste para verificar a requisição POST para criar um aniversario utilizando
        uma data de aniversario inexistente"""

        data = {
            'nome': 'Billy Preston',
            'data_aniversario': '02/09/3000'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_delete_para_deletar_aniversario(self):
        """ Teste para verificar a requisição DELETE para deletar um aniversário """

        response = self.client.delete('/aniversarios/1/')
        self.assertAlmostEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_aniversario(self):
        """ Teste para verificar a requisição PUT para atualizar um curso """

        data = {
            'nome': 'Richard Starkey',
            'data_aniversario': '07/07/1940'
        }

        response = self.client.put('/aniversarios/4/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_put_para_atualizar_aniversario_atributo_errado(self):
        """ Teste para verificar a requisição PUT para atualizar um curso
        com nome de atributo errado """

        data = {
            'nome': 'Richard Starkey',
            'data_nascimento': '07/07/1940',
        }

        response = self.client.put('/aniversarios/4/', data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_put_para_atualizar_aniversario_id_inexistente(self):
        """ Teste para verificar a requisição PUT para atualizar um curso
        com id enexistente """

        data = {
            'nome': 'Richard Starkey',
            'data_aniversario': '07/07/1940',
        }

        response = self.client.put('/aniversarios/8000/', data=data)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)