from django.test import TestCase
from .models import Category, Blog, Profile, Comment

class CategoryModelTest(TestCase):
    def test_sample_category(self):
        test_object = Category.objects.create(name='sample-category')
        self.assertEqual(test_object.name, 'sample-category')

class BlogModelTest(TestCase):
    def test_sample_blog(self):
        test_object = Blog.objects.create(title='sample-blog', content='sample-content')
        self.assertEqual(test_object.title, 'sample-blog')
        self.assertEqual(test_object.content, 'sample-content')

class ProfileModelTest(TestCase):
    def test_sample_profile(self):
        test_object = Profile.objects.create(user='sample-user')
        self.assertEqual(test_object.user, 'sample-user')

class CommentModelTest(TestCase):
    def test_sample_comment(self):
        test_object = Comment.objects.create(content='sample-comment')
        self.assertEqual(test_object.content, 'sample-comment')

# Create your tests here.
