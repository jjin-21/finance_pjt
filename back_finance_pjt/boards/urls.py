from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('',views.board_list),
    path('<int:board_pk>/',views.board_detail),
    path('<int:board_pk>/likes/', views.board_likes),
    path('comments/',views.comment_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('<int:board_pk>/comments/', views.comment_create),
    # path('', views.index, name='index'),
    # path('create/', views.create, name='create'),
    # path('<int:pk>/detail/', views.detail, name='detail'),
    # path('<int:pk>/update/', views.update, name='update'),
    # path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/comment/', views.create_comment, name='create_comment'),
    # path('<int:board_pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    # path('<int:board_pk>/comment/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
]
