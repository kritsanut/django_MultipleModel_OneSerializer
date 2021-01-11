# url in app #

from django.urls import include, path
from . import views


urlpatterns = [
    ....
    path('mainmenu/filters', views.get_all)
    ....
]
