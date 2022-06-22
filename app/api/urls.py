# app/api/urls.py

from django.urls import path
from app.api.views import (
    ArticleListCreateAPIView,
    ArticleDetailAPIView,
    RecruiterListCreateAPIView,
    ApplyListCreateAPIView
)

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list"),
    path("articles/<int:pk>", ArticleDetailAPIView.as_view(), name="article-detail"),
    path("recruiters/", RecruiterListCreateAPIView.as_view(), name="recruiter-list"),
    path("applies/", ApplyListCreateAPIView.as_view(), name="apply-list")
]