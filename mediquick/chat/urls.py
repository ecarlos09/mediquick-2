# from django.urls import path, include
# from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
# from rest_framework.routers import DefaultRouter
# from .api import MessageModelViewSet, UserModelViewSet

# from . import views

# router = DefaultRouter()
# router.register(r'message', MessageModelViewSet, basename='message-api')
# router.register(r'user', UserModelViewSet, basename='user-api')

# urlpatterns = [
#     # path('', views.index, name='index'),
#     # path('<str:room_name>/', views.room, name='room'),
#     path(r'api', include(router.urls)),

#     path('', login_required(
#         TemplateView.as_view(template_name='chat/chat.html')), name='home'),
# ]
  
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    url(r'logout/', views.logout),
]