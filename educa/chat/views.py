from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
# from .models import Message



@login_required
def course_chat_room(request, course_id):
     try:
         # retrieve course with given id joined by the current user
         course = request.user.courses_joined.get(id=course_id)
         # username = request.GET.get('username', 'Anonymous')
         # messages = Message.objects.filter(room=course_id)[0:25]
     except:
         # user is not a student of the course or course does not exist
         return HttpResponseForbidden()
     return render(request, 'chat/room.html', {'course': course,})
# 'room': course_id, 'username': username, 'messages': messages }






# def index(request):
#     return render(request, 'chat/index.html')
#
# def room(request, room_name):
#     # username = request.GET.get('username', 'Anonymous')
#     messages = Message.objects.filter(room=room_name)[0:25]
#
#     return render(request, 'room.html', {'messages': messages})