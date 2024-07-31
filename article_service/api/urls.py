from django.urls import path

from api.views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleUpdateView,
    PrivateArticleListView,
    PublicArticleListView,
    UserCreateView,
)

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path(
        "articles/public/",
        PublicArticleListView.as_view(),
        name="public-articles",
    ),
    path(
        "articles/private/",
        PrivateArticleListView.as_view(),
        name="private-articles",
    ),
    path(
        "articles/create/", ArticleCreateView.as_view(), name="article-create"
    ),
    path(
        "articles/update/<int:pk>/",
        ArticleUpdateView.as_view(),
        name="article-update",
    ),
    path(
        "articles/delete/<int:pk>/",
        ArticleDeleteView.as_view(),
        name="article-delete",
    ),
]
