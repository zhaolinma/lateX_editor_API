from rest_framework import generics,permissions
from .models import Article
from .serializers import ArticleSerializer
from .permissions import isOwnerOrReadOnly


class ArticleList(generics.ListCreateAPIView):
    permission_classes = (isOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isOwnerOrReadOnly,permissions.IsAuthenticated)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
