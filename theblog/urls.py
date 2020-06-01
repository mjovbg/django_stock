from django.urls import path
# from . import views
from .views import BlogView, ArticleDetailView, AddPostView

urlpatterns = [
    # path('', views.blog, name = 'blog'),
    path('', BlogView.as_view(), name='blog'),             # this is how you import class based view
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
]