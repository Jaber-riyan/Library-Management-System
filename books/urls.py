from django.urls import path
from .import views


urlpatterns = [
    path('detailview/<int:pk>/', views.DetailViewOfBook.as_view(), name='detailview'),
    path('borrow_book/<int:id>/',views.borrowHistory, name='borrowbook'),
    path('profile/<int:id>/',views.profile,name='profile'),
    path('return_book/<int:id>/', views.return_book, name='return_book'),
]
