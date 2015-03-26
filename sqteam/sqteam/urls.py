from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import handler404
from rest_framework import routers

from sqapp.views import SqUserViewSet, ProjectViewSet, NewsViewSet


router = routers.DefaultRouter()
router.register(r'users', SqUserViewSet, base_name='users')
router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'news', NewsViewSet, base_name='news')


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^$', 'sqapp.views.index', name='index'),
    url(r'^user/login/', 'sqapp.views.login_func', name='login'),
    url(r'^login/', 'sqapp.views.login_view', name='login view'),
    url(r'^logout/', 'sqapp.views.logout_func', name='logout'),
    url(r'^user/signup/', 'sqapp.views.signup_func', name='signup'),
    url(r'^signup/', 'sqapp.views.signup_view', name='signup view'),
    url(r'^app/', 'sqapp.views.app_view', name='app'),

    #url(r'^subscribe/(?P<project_id>\d+)', 'sqapp.views.subscribe', name='subscribe'),
    url(r'^subscribe/', 'sqapp.views.subscribe', name='subscribe'),
    url(r'^news/(?P<project_id>\d+)', 'sqapp.views.get_news', name='news'),
    url(r'^search', 'sqapp.views.search', name='search'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


)