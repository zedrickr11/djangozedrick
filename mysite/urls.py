from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    #url(r'^accounts/login/$', views.login, name='login'),
    #url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),

    path('admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),

    path('', include('blog.urls')),
]
