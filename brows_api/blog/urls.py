from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', HomeStoreListView.as_view()),
    path('portfolio/', WorkPhotoListView.as_view()),
    path('blog/', PostListView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view()),
    path('blog/add-post/', PostCreateView.as_view()),
    path('portfolio/add-photo/', WorkPhotoCreateView.as_view()),
    path('post/<str:slug>/update/', PostUpdateDestroyView.as_view()),
    path('portfolio/<str:slug>/update/', WorkPhotoUpdateDestroyView.as_view()),
    path('event/', EventCreateView.as_view()),

]