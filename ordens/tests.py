from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase

from .utils import apenas_digitos, validar_cpf


class CPFUtilsTests(TestCase):
    def test_apenas_digitos_remove_pontuacao(self):
        self.assertEqual(apenas_digitos('529.982.247-25'), '52998224725')

    def test_validar_cpf_aceita_cpf_valido(self):
        self.assertEqual(validar_cpf('529.982.247-25'), '52998224725')


class CPFBackendTests(TestCase):
    def test_login_aceita_cpf_formatado(self):
        User = get_user_model()
        User.objects.create_user(
            cpf='52998224725',
            password='Senha#123',
            nome_completo='Cliente Teste',
            telefone='83999990000',
        )

        usuario = authenticate(username='529.982.247-25', password='Senha#123')
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.cpf, '52998224725')
