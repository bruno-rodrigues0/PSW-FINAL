from django.urls import path
from . import views

app_name = "questions"
urlpatterns = [
    path("", views.questions_list, name="questions_list"),
    path("create/", views.questions_create, name="questions_create"),
    path("<int:pk>/", views.questions_detail, name="questions_detail"),
    path("<int:pk>/edit/", views.questions_update, name="questions_update"),
    path("<int:pk>/delete/", views.questions_delete, name="questions_delete"),
]
