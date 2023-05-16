# # from django.shortcuts import render, redirect
# # from chat.models import Room, Message
# # from django.http import HttpResponse, JsonResponse

# # # Create your views here.
# # def chat_home(request):

# #     if request.method =='POST':
# #        room = request.POST['room_name']
# #        username = request.POST['username']

# #        if Room.objects.filter(name=room).exists():
# #             return redirect('/'+room+'/?username='+username)
# #        else:
# #            new_room = Room.objects.create(name=room)
# #            new_room.save()
# #            return redirect('/'+room+'/?username='+username)

# #     return render(request, 'Chat/chat_home.html')

# # def room(request, room):
# #     username = request.GET.get('username')
# #     room_details = Room.objects.get(name=room)
# #     return render(request, 'Chat/chat_room.html', {
# #         'username': username,
# #         'room': room,
# #         'room_details': room_details
# #     })


    

# # def send(request):
# #     message = request.POST['message']
# #     username = request.POST['username']
# #     room_id = request.POST['room_id']

# #     new_message = Message.objects.create(value=message, user=username, room=room_id)
# #     new_message.save()
# #     return HttpResponse('Message sent successfully')

# # def getMessages(request, room):
# #     room_details = Room.objects.get(name=room)

# #     messages = Message.objects.filter(room=room_details.id)
# #     return JsonResponse({"messages":list(messages.values())})

# from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# from django.shortcuts import get_object_or_404, render, redirect
# from django.views import View
# from django.contrib.auth.models import User

# from Schoolapp.models import tbl_login
# from .models import Message

# @login_required(login_url='login')
# def chat_view(request, recipient_id):
#     email = request.session['email'] 
#     user = tbl_login.objects.get(email=email)
#     recipient = get_object_or_404(tbl_login, id=recipient_id)
#     messages = Message.objects.filter(Q(sender=user, recipient=recipient) | Q(sender=recipient, recipient=user)).order_by('timestamp')
#     context = {'recipient': recipient, 'messages': messages}
#     return render(request, 'Chat/chat.html', context)


# @login_required(login_url='login')
# def send_message_view(request, recipient_id):
#     recipient = get_object_or_404(tbl_login, id=recipient_id)
#     if request.method == 'POST':
#         email = request.session['email'] 
#         user = tbl_login.objects.get(email=email)
#         message = request.POST.get('message')
#         if message:
#             Message.objects.create(sender=user, recipient=recipient, message=message)
#             return redirect('chat', recipient_id=recipient_id)
#     context = {'recipient': recipient}
#     return render(request, 'Chat/send_message.html',context)



from django.shortcuts import render
from Schoolapp.models import tbl_login, teacher_detail
from chat.models import Message



def chat_view(request, sender_id, receiver_id):
    sender = tbl_login.objects.get(id=sender_id)
    receiver = teacher_detail.objects.get(id=receiver_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        message_obj = Message(sender=sender, receiver=receiver, message=message)
        message_obj.save()
    messages = Message.objects.filter(sender=sender, receiver=receiver) | Message.objects.filter(sender=receiver, receiver=sender)
    context = {'sender': sender, 'receiver': receiver, 'messages': messages}
    return render(request, 'Chat/chat.html', context)

