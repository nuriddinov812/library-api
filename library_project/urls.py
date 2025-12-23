from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter


urlpatterns = [
    
    # path('', views.BookListApiView.as_view(), name='book-list'),
    # path('create/', views.BookCreateApiView.as_view(), name='book-create'),
    # path('<int:pk>/', views.BookDetailApiView.as_view(), name='book-detail'),
    # path('<int:pk>/delete', views.BookDeleteApiView.as_view(), name='book-delete'),
    # path('<int:pk>/update', views.BookUpdateApiView.as_view(), name='book-update'),
    
    # # efficient ways
    # path('list-create/', views.BookListCreateApiView.as_view(), name='book-list-create'),
    # path('detail/<int:pk>/', views.BookDeleteUpdateApiView.as_view(), name='book-detail-update-delete'),
    
]

# Yuqoridagi viewset uchun router yaratish
router = SimpleRouter()
router.register('', views.BookViewSet, basename='book')

urlpatterns += router.urls 