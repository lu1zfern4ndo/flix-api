import json
import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


# Função auxiliar para criar um usuário, gerar um token JWT e retornar o token
@pytest.mark.django_db
def get_auth_token(username, password):
    user = User.objects.create(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)


# Teste real que usao o token JWT para fazer uma solicitação autenticada a um endpoint protegiro
@pytest.mark.django_db
def test_authenticated_endpoint():
    # Criar um usuário para autenticação
    username = 'testuser'
    password = 'testuser'
    auth_token = get_auth_token(username, password)

    # Configurar o cliente de teste
    client = APIClient()

    # Configurar o cabeçalho de autenticação
    headers = {'Authorization': f'Bearer {auth_token}'}

    # Fazer uma solicitação autenticada ao seu endpoint protegido
    response = client.get('http://localhost:8000/api/v1/reviews/', headers=headers)

    # Vertificar se a resposta é 200 OK (ou outro código de sucesso)
    assert response.status_code == status.HTTP_200_OK
