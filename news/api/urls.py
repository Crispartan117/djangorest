from django.urls import path
from news.api.views import (ArticleListCreateAPIView,
                            ArticleDetailCreateAPIView,
                            JournalistListCreateAPIView)
#from news.api.views import (article_list_create_api_view, 
#                            article_detail_create_view)

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailCreateAPIView.as_view(), name="article-detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="journalist-list")
]



#   path("articles/", article_list_create_api_view, name="article-list"),
#   path("articles/<int:pk>/", article_detail_create_view, name="article-detail")