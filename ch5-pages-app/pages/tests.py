from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTest(SimpleTestCase):
    def test_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

