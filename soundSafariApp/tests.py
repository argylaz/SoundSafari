from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewTestCase(TestCase):
    def setUp(self):
        # Set up data for tests
        self.username = 'testuser'
        self.password = '12345'
        User.objects.create_user(username=self.username, password=self.password)

    def test_index_view_status_code(self):
        # Test that the index page can be accessed.
        response = self.client.get(reverse('soundSafariApp:index'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_status_code(self):
        # Test that the about page can be accessed.
        response = self.client.get(reverse('soundSafariApp:about'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_success(self):
        # Test logging in with correct credentials.
        response = self.client.post(reverse('soundSafariApp:user_login'), {'username': self.username, 'password': self.password})
        self.assertRedirects(response, reverse('soundSafariApp:index'))

    def test_user_login_fail(self):
        # Test logging in with incorrect credentials.
        response = self.client.post(reverse('soundSafariApp:user_login'), {'username': self.username, 'password': 'wrongpassword'})
        self.assertIn(b"Invalid login details supplied.", response.content)

class UserRegistrationTestCase(TestCase):
    def test_user_registration_success(self):
        # Data for a new user registration
        new_user_data = {
            'username': 'newuser',
            'password1': 'complexpassword',
            'password2': 'complexpassword',  # Confirmation password
            'email': 'newuser@example.com'
        }

        # Post the data to the registration view
        response = self.client.post(reverse('soundSafariApp:register'), data=new_user_data)
        
        # Check redirect to index page
        self.assertRedirects(response, reverse('soundSafariApp:index'))
        
        # Check user count in database increased by 1
        self.assertEqual(User.objects.count(), 1)

    def test_user_registration_failure(self):
        # Data with a missing field (e.g., email)
        incomplete_data = {
            'username': 'newuser',
            'password1': 'complexpassword',
            'password2': 'complexpassword'  # Missing email
        }

        # Attempt to post the incomplete data
        response = self.client.post(reverse('soundSafariApp:register'), data=incomplete_data)
        
        # Check that the response indicates a form error 
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].errors)
        
        # Ensure no new user was created
        self.assertEqual(User.objects.count(), 0)