from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls import handler404
from sqapp import error_views, views

urlpatterns = patterns('',
    url(r'^$', 'sqapp.views.index', name='index'),
    url(r'^user/login/', 'sqapp.views.login_func', name='login'),
    url(r'^login/', 'sqapp.views.login_view', name='login view'),
    url(r'^logout/', 'sqapp.views.logout_func', name='logout'),
    url(r'^user/signup/', 'sqapp.views.signup_func', name='signup'),
    url(r'^signup/', 'sqapp.views.signup_view', name='signup view'),
    url(r'^app/', 'sqapp.views.app_view', name='app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


)
handler404 = views.index
handler405 = 'sqapp.error_views.method_not_allowed'