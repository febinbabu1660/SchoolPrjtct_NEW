# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('chathome/', views.chat_home, name='chathome'),
#     # path('<str:room>/', views.room, name='room'),
#     # # path('checkview/', views.checkview, name='checkview'),
#     # path('send', views.send, name='send'),
#     # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
#     # path('chat/<int:recipient_id>/', views.chat_view, name='chat'),
#     # path('send_message/<int:recipient_id>/', views.send_message_view, name='send_message'),
# ]

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('chat/<int:sender_id>/<int:receiver_id>/', views.chat_view, name='chat_view'),
]
