from django.urls import path

from .views import api, site

app_name = 'blog'

urlpatterns = [
    path('', site.index, name="index"),
    path('detalhes/<int:pk>/<slug:slug>', site.detail, name="details"),
    path('post/novo/', site.post, name="new_post"),
    path('editar/post/<int:pk>', site.edit, name="edit"),
    path('filter/<int:pk>/<str:username>', site.filter, name="filter"),
    path('search/', site.search, name="search"),
    path('delete/<int:pk>', site.delete, name="delete_post"),
    path('contato/', site.contato, name="contato"),

    path('posts/api/v1/', api.post_api_list, name="post_api_v1"),
    path('posts/api/v1/<int:pk>', api.post_api_detail,
         name="post_api_v1_detail"),
]
