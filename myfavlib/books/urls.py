from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>_<int:num>', views.index, name='index_mod'),
    path('<int:book_id>/detail/', views.detail),
    path('genre/', views.genres, name='genre'),
    path('genre/<str:genre_name>', views.genre_detail),
    path('about/', views.about, name='about')
]
