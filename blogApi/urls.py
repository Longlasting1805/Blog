from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import BlogApiView, blogDetailApi, commentView

router = DefaultRouter()
# router.register('blog', BlogApiView, basename='blog')

urlpatterns = [
    path('/', include(router.urls)),
    # path('detail/<int:id>/', BlogApiView.as_view()),
    path('blog/', BlogApiView.as_view()),
    path('blogDetail/', blogDetailApi.as_view()),
    path('comment/', commentView.as_view())
]
