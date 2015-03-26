from django.core import mail
from django.test import TestCase, Client
from django.utils import timezone
from sqapp.models import Project, SqUser, News

from django.test.utils import setup_test_environment
setup_test_environment()

class ProjectTestCase(TestCase):
    def setUp(self):
        Project.objects.create(topic=Project.TOPICCHOICE[0],
                               help_type=Project.TOPICCHOICE[0],
                               location=Project.LOCATIONCHOICE[0],
                               name='project1')
        Project.objects.create(topic=Project.TOPICCHOICE[2],
                               help_type=Project.TOPICCHOICE[2],
                               location=Project.LOCATIONCHOICE[2],
                               name='project2')

    def test_project_creation(self):
        """Project do not have subscribers and serialization works well"""
        pr1 = Project.objects.get(name='project1')
        pr2 = Project.objects.get(name='project2')
        self.assertQuerysetEqual(pr1.subscribers.all(), [])
        self.assertIn('id', pr2.serialize().keys())
        self.assertNotIn('project1', pr2.serialize().values())


class NewsTestCase(TestCase):
    def setUp(self):
        self.now = timezone.now()
        self.long_string = 'news2 very long news string longer that forty characters to test string trimming'
        self.new1_id = News.objects.create(date=self.now, text='news1').id
        self.new2_id = News.objects.create(date=self.now, text=self.long_string).id
        mail.outbox = []
        self.user_mail = 'user@gmail.com'

    def test_news_creation(self):
        """Test news for creation and representation"""
        news1 = News.objects.get(text='news1')
        news2 = News.objects.get(pk=self.new2_id)
        self.assertEqual(news1.text, 'news1')
        self.assertEqual(news1.date, self.now)
        self.assertEqual(str(news2), self.long_string[:40])


    def test_news_mailing(self):
        project = Project.objects.create(topic=Project.TOPICCHOICE[0],
                                         help_type=Project.TOPICCHOICE[0],
                                         location=Project.LOCATIONCHOICE[0],
                                         name='project')
        user = SqUser.objects.create_user(self.user_mail, 'nopassword')
        project.subscribers.add(user)
        new_notice = News.objects.create(text='New notice', project=project)
        """One for new user alert and another subscription notifier"""
        self.assertEqual(len(mail.outbox), 2)
        recepients = mail.outbox[0].recipients()

        self.assertIn(self.user_mail, recepients)
        self.assertIn('E-mail', mail.outbox[0].body)
        self.assertIn(new_notice.text, mail.outbox[1].body)


class AppViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_guest_user(self):
        response = self.client.get('/')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, u'Volun Deer', status_code=200)
        self.assertContains(response, u'sq team', status_code=200)
