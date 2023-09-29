from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from users.forms import UserRegistrationForm


class UserRegostrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        data = {'first_name': 'serj', 'last_name': 'boytsov,', 'email': 'ser@mail.ru', 'password1': 'qwerty26',
                'password2': 'qwerty26'}
        response = self.client.post(self.path, data=data)
