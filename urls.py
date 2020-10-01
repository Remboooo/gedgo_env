from django.conf.urls import include, url
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import admin

import django.contrib.auth.views

admin.autodiscover()

urlpatterns = [ 
    url(r'^$', lambda r: redirect('/gedgo/')),
    url(r'^gedgo/', include('gedgo.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$',
        django.contrib.auth.views.LoginView.as_view(),
        {'template_name': 'auth/login.html'}),
    url(r'^login/$',
        django.contrib.auth.views.LoginView.as_view(),
        {'template_name': 'auth/login.html'},
        name='login',
    ),
    url(r'^robots\.txt$',
        lambda r: HttpResponse(
            "User-agent: *\nDisallow: /",
            mimetype="text/plain"))
]
