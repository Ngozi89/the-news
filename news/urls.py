from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.about, name="about"),
    path('policy', views.policy, name="policy"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('comments/<int:pk>/update/', views.UpdateComment.as_view(), name='edit'),
    path('comments/<int:pk>/delete/', views.DeleteComment.as_view(), name='delete'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_ads>', views.add_ads(), name='ads'),
]
