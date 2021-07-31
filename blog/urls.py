from django.urls import path
from .views import HomeListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/create', BlogCreateView.as_view(), name='post_new'),
]