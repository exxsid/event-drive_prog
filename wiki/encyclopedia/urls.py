from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("search/", views.search_page, name="search"),
    path("createnewpage/", views.create_new_page, name="create_new_page"),
    path("editpage/<str:title>", views.edit_page, name="edit_page"),
    path("randompage/", views.random_page, name="random_page")
]
