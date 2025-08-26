from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    path("", views.community_list, name="community_list"),
    path("create/", views.community_create, name="community_create"),
    path("<int:pk>/", views.community_detail, name="community_detail"),
    path("<int:pk>/edit/", views.community_update, name="community_update"),
    path("<int:pk>/delete/", views.community_delete, name="community_delete"),
]
