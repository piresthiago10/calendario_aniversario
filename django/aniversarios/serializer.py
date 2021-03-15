from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from datetime import datetime

from aniversarios.models import Aniversario
from aniversarios.validators import *


class AniversarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aniversario
        fields = '__all__'

    def validate(self, data):
        """ Valida nome e data de aniversário """

        # remove os espaços da variavel nome para
        # não gerar conflito com o validador de nome
        nome = data['nome'].replace(" ", "")
        data_aniversario = datetime.strptime(
            data['data_aniversario'], '%d/%m/%Y').date()
        print(f"data {data_aniversario}")
        if not nome_valido(nome):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo"})

        if not data_aniversario_valido(data_aniversario):
            raise serializers.ValidationError(
                {'data_aniversario': "A data de aniversario não pode ser maior do que hoje."})
        return data
