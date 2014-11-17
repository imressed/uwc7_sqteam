from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'sqapp.views.index', name='index'),
    url(r'^login/', 'sqapp.views.login_view', name='login'),
    url(r'^logout/', 'sqapp.views.logout_view', name='logout'),
    url(r'^signup/', 'sqapp.views.signup_view', name='signup'),
    url(r'^app/', 'sqapp.views.app_view', name='app'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
