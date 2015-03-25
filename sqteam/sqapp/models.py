from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)


class SqUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class SqUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'

    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    projects = models.ManyToManyField('Project', null=True, blank=True)

    REQUIRED_FIELDS = []

    objects = SqUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Project(models.Model):



    TOPICCHOICE = (
        (u'Допомога престарілим', u'Допомога престарілим'),
        (u'Допомога тваринам', u'Допомога тваринам'),
        (u'Тварина програмісту', u'Тварина програмісту'),
        (u'Престарілим тварину', u'Престарілим тварину'),
    )

    LOCATIONCHOICE = (
        (u'Київ', u'Київ'),
        (u'Вінниця', u'Вінниця'),
        (u'Львів', u'Львів'),
    )

    TYPECHOICE = (
        (u'Матеріально', u'Матеріально'),
        (u'Часом', u'Часом'),
        (u'Кодом', u'Кодом'),
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=100, choices=TOPICCHOICE)
    location = models.CharField(max_length=100, choices=LOCATIONCHOICE)
    help_type = models.CharField(max_length=100, choices=TYPECHOICE)
    subscribers = models.ManyToManyField('SqUser', null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'topic': self.topic,
            'location': self.location,
            'help_type': self.help_type
        }


class News(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200)
    project = models.ForeignKey('Project', null=True, blank=True)

    def __str__(self):
        return self.text[:40]

    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime('%H:%M %d/%b/%y'),
            'text': self.text
        }