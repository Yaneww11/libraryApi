from django.urls import path, include
from rest_framework.routers import DefaultRouter

from libraryApi.books import views


router = DefaultRouter()
router.register('', views.PublisherViewSet)

urlpatterns = [
    path('books/', views.ListBookView.as_view(), name='books_list'),
    path('books/<int:pk>/', views.DetailBookView.as_view(), name='book_viewSET'),
    path('demo/', views.demo),
    path('publisher-links/', views.PublisherHyperLinkedView.as_view(), name='publisher_links'),
    path('publishers/', include(router.urls)),
]