from django.conf.urls import patterns, include, url
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.contrib import admin

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request,user):
        return '/rango/'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/password/change/$', MyRegistrationView.as_view(), name='password_change_form'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}),
    )