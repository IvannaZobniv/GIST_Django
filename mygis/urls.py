"""GIST URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
import mygis.views



def rstatic(STATIC_URL, document_root) -> object:
    pass


def static(MEDIA_URL, document_root) -> object:
    pass


urlpatterns = [
    url(r'^$', mygis.views.home, name='home'),
    url(r'^map/$', mygis.views.map_my, name='map'),
    url(r'^about/$', mygis.views.about, name='about'),
    url(r'^articles/(?P<article_id>[0-9]+)/$', mygis.views.show_articles, name='article'),

]

