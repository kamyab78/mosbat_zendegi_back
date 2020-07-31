from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mosbat@.com',
            password='admin12345',
            username='admin'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@mosbat.com',
            password='pass12345',
            username='user'
        )
