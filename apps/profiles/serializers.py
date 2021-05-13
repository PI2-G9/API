from rest_framework import serializers

from apps.profiles.models import Profile


class ProfilePhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nome', 'photo', 'cpf']


class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['cpf', 'nome', 'data_nascimento', 'telefone', 'photo', 'is_employee', 'objects', 'endereco_cep',
                  'endereco_nome_rua', 'endereco_complemento', 'endereco_numero', 'endereco_nome_cidade',
                  'endereco_estado']
