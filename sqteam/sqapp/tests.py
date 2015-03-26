from datetime import datetime
from django.test import TestCase
from django.utils import timezone
from sqapp.models import Project, SqUser, News


#class ProjectTestCase(TestCase):
#    def setUp(self):
#        Project.objects.create(name="lion", sound="roar")
#        Project.objects.create(name="cat", sound="meow")
#
#    def test_animals_can_speak(self):
#        """Animals that can speak are correctly identified"""
#        lion = Animal.objects.get(name="lion")
#        cat = Animal.objects.get(name="cat")
#        self.assertEqual(lion.speak(), 'The lion says "roar"')
#        self.assertEqual(cat.speak(), 'The cat says "meow"')


class NewsTestCase(TestCase):
    def setUp(self):
        self.now = timezone.now()
        self.long_string = 'news2 very long news string longer that forty characters to test string trimming'
        self.new1_id = News.objects.create(date=self.now, text='news1').id
        self.new2_id = News.objects.create(date=self.now, text=self.long_string).id

    def test_news_creation(self):
        """Test news for creation and representation"""
        news1 = News.objects.get(text='news1')
        news2 = News.objects.get(pk=self.new2_id)
        self.assertEqual(news1.text, 'news1')
        self.assertEqual(news1.date, self.now)
        self.assertEqual(str(news2), self.long_string[:40])