from unittest import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):

        password = 'test12345'
        username = 'test'
        user = get_user_model().objects.create_user(
            password=password,
            username=username
        )
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        username = 'test'
        user = get_user_model().objects.create_user(
                                                    username, 'test12345')
        self.assertEqual(user.username, username.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username=None,
                password='test12345'
            )

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            email='test@mosbat.com',
            username='test',
            password='test12345'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
