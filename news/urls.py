from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('addarticles/', views.AddArticle.as_view(), name='add_article'),
    path('browsearticles/', views.PostList.as_view(), name='browse_article'),
    path("myarticle/", views.MyArticle.as_view(), name="my_article"),
    path('about', views.about, name="about"),
    path('policy', views.policy, name="policy"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>/update/', views.UpdateComment.as_view(), name='edit'),
    path('comments/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete'),
    path('articles/<int:pk>/delete/', views.DeleteArticle.as_view(), name='delete_article'),
    path('comments/<int:pk>/reply/', views.ReplyComment.as_view(), name='reply'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path('articles/<slug:slug>/edit/', views.EditArticle.as_view(), name='edit_article'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
