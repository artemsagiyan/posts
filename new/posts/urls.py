from django.urls import path

from .views import PostView, CommentView

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('post/<int:pk>/comment/', CommentView.as_view()),
]