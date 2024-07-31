from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthorOrReadOnly
from api.serializers import ArticleSerializer, UserSerializer
from articles.models import Article
from users.models import User


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PublicArticleListView(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=True)
    serializer_class = ArticleSerializer


class PrivateArticleListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(
            is_public=False, author=self.request.user
        )


class ArticleCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
