from django.urls import path
from . import views

app_name = 'anonymous_boards'
urlpatterns = [
    path('',views.board_list),
    path('<int:board_pk>/',views.board_detail),
    path('<int:board_pk>/likes/', views.board_likes),
    path('comments/',views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('<int:board_pk>/comments/', views.comment_create),
]