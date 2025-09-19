from django.urls import path

from .views import *

app_name = 'sunnats'

urlpatterns = [
    path('', view=index, name='index'),
    path('category/<slug>', view=category, name='category'),
    path('biographies/', view=biographies, name='biographies'),
    path('about/', view=about, name='about'),
]