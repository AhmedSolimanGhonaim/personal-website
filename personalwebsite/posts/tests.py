from django.test import TestCase 
from .models import Posts
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Posts.objects.create(text="This is a test!")
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")