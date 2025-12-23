from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListApiView.as_view(), name='book-list'),
    path('create/', views.BookCreateApiView.as_view(), name='book-create'),
    path('<int:pk>/', views.BookDetailApiView.as_view(), name='book-detail'),
    path('<int:pk>/delete', views.BookDeleteApiView.as_view(), name='book-delete'),
    path('<int:pk>/update', views.BookUpdateApiView.as_view(), name='book-update'),
    
    # efficient ways
    path('list-create/', views.BookListCreateApiView.as_view(), name='book-list-create'),
    path('detail/<int:pk>/', views.BookDeleteUpdateApiView.as_view(), name='book-detail-update-delete'),
    
]