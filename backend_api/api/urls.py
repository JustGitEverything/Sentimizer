from django.urls import path
from . import views
urlpatterns = [
    path('', views.diary_entry, name="diary_entry"),
]