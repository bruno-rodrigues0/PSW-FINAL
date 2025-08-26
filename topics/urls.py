from django.urls import path
from . import views

app_name = "topics"
urlpatterns = [
    path("", views.topics_list, name="topics_list"),
    path("create/", views.topics_create, name="topics_create"),
    path("<int:pk>/", views.topics_detail, name="topics_detail"),
    path("<int:pk>/edit/", views.topics_update, name="topics_update"),
    path("<int:pk>/delete/", views.topics_delete, name="topics_delete"),
]