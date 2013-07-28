from django.conf.urls import patterns, include, url
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', lambda r: redirect('/gedgo/')),
    url(r'^gedgo/', include('gedgo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'gedgo/login.html'}),
    url(r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-agent: *\nDisallow: /",
            mimetype="text/plain"))
)
