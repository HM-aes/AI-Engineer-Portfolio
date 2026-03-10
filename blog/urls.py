from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog-list"),
    path("feed/", views.LatestEntriesFeed(), name="blog-feed"),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="blog-detail"),
]
