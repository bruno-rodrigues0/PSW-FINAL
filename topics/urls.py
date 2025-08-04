from django.urls import path
from . import views

app_name = "topics"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/<int:id_comment>", views.update, name="update"),
    path("delete/<int:id_comment>", views.delete, name="delete"),
    path("detail/<int:id_comment>", views.detail, name="detail"),
]
