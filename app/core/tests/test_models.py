from unittest import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email='test@mosbat.com'
        password='test12345'
        username='test'
        user=get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )
        self.assertEqual(user.email , email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email='test@MOSBAT.COM'
        username='test'
        user=get_user_model().objects.create_user(email,username,'test12345')
        self.assertEqual(user.email , email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None ,
                username=None ,
               password= 'test12345')

    def test_create_new_superuser(self):
        user=get_user_model().objects.create_superuser(
            email='test@mosbat.com',
            username='test',
            password='test12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

