from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient

from .models import Comic

User = get_user_model()


class RatingAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.client.force_authenticate(user=self.user2)
        self.comic = Comic.objects.create(title='Test Comic', author='Test Author')

    def test_create_rating_and_update_comic_rating(self):
        response = self.client.post('/api/rating/', {'comic_id': self.comic.id, 'user_id': self.user.id, 'VALUE': 4})
        self.assertEqual(response.status_code, 201)

        updated_comic = Comic.objects.get(id=self.comic.id)
        self.assertEqual(updated_comic.rating, 4.0)

        response = self.client.post('/api/rating/', {'comic_id': self.comic.id, 'user_id': self.user.id, 'VALUE': 5})
        self.assertEqual(response.status_code, 201)

        updated_comic = Comic.objects.get(id=self.comic.id)
        self.assertEqual(updated_comic.rating, 5)

    def test_get_average_comic_rating(self):
        self.client.post('/api/rating/', {'comic_id': self.comic.id, 'user_id': self.user.id, 'VALUE': 1})
        self.client.post('/api/rating/', {'comic_id': self.comic.id, 'user_id': self.user2.id, 'VALUE': 5})

        response = self.client.get(f'/api/comics/{self.comic.id}/rating/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['rating'], '3.00')
