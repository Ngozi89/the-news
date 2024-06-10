from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addarticles/', views.AddArticle.as_view(), name='add_article'),
    path('about', views.about, name="about"),
    path('policy', views.policy, name="policy"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>/update/', views.UpdateComment.as_view(), name='edit'),
    path('comments/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete'),
    path('comments/<int:pk>/reply/', views.ReplyComment.as_view(), name='reply'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path('posts/<slug:slug>/edit/', views.EditArticle.as_view(), name='edit_article'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
