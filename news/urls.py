from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("browsearticles/", views.PostList.as_view(), name="browse_article"),
    path("addarticle/", views.AddArticle.as_view(), name="add_article"),
    path("myarticles/", views.MyArticle.as_view(), name="my_article"),
    path("bookmark/", views.Bookmarked.as_view(), name="bookmarked"),
    path("about/", views.about, name="about"),
    path("policy/", views.policy, name="policy"),
    path("comments/<int:pk>/edit/", views.EditComment.as_view(), name="edit_comment"),
    path("comments/<int:pk>/delete/", views.DeleteComment.as_view(), name="delete_comment"),
    path("article/<int:pk>/delete/", views.DeleteArticle.as_view(), name="delete_article"),
    path("bookmarks/<slug:slug>/", views.PostBookmark.as_view(), name="post_bookmark"),
    path("likes/<slug:slug>/", views.PostLike.as_view(), name="post_like"),
    path("postdetail/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("article/<slug:slug>/edit/", views.EditArticle.as_view(), name="edit_article"),
    path("profile/<int:pk>/", views.Profile.as_view(), name="profile"),
]
