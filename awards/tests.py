from django.test import TestCase

from django.test import TestCase
from .models import Profile,Projects
from django.contrib.auth.models import User


class ProfileTest(TestCase):
    def setUp(self):
        self.dorcas = User(username = 'Dorcas',email = 'dorcasmosonik@gmail.com')
        self.dorcas = Profile(user = Self.dorcas,user = 1,Bio = 'tests',photo = 'test.jpg',date_craeted='dec,01.2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.dorcas,Profile))

    def test_save_profile(self):
        Profile.save_profile(self)
        all_profiles = Profile.objects.all()
        self.assertTrue(len(all_profiles),0)

    def test_delete_profile(self):
        self.dorcas.delete_profile()
        all_profiles = Profile.objects.all()
        self.assertEqual(len(all_profiles),0)



class ProjectsTestCase(TestCase):
    def setUp(self):
        self.new_post = Projects(title = 'testT',projectscreenshot = 'test.jpg',description = 'testD',user = peris,projecturl = 'https://test.com',datecreated='Dec,01.2020')


    def test_save_project(self):
        self.new_post.save_project()
        pictures = Image.objects.all()
        self.assertEqual(len(pictures),1)

    def test_delete_project(self):
        self.new_post.delete_project()
        pictures = Projects.objects.all()
        self.assertEqual(len(pictures),1)  
