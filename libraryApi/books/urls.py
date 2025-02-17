from django.urls import path

from libraryApi.books import views

urlpatterns = [
    path('books/', views.ListBookView.as_view()),
    path('books/<int:pk>/', views.DetailBookView.as_view())
]