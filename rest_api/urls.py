from django.urls import path
from .views import PostsView, posts_detail, PostsAPIView, postDetailsAPIView, genericApiView

urlpatterns = [
    # path('posts/', PostsView),
    # path('details/<int:pk>', posts_detail),

    # path('postsApiView/', PostsAPIView.as_view()),
    # path('detailsApiView/<int:pk>', postDetailsAPIView.as_view()),

    path('genericApiView/<int:id>', genericApiView.as_view()),

]