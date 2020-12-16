from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Board
from .models import Topic
from .models import Post
from django.contrib.auth.models import User
# Create your views here.


def home(request):

    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})


def board_topics(request,board_id):
    try:
        board = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        return render(request,'error404.html')

    return render(request,'topics.html',{'board':board})

def new_topic(request,board_id):

    try:
        board = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        return render(request,'error404.html')

    if request.method =="POST":
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            create_by=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            create_by=user
        )
        return redirect("board_topics",board_id=board.pk)
    return render(request, 'new_topic.html',{'board':board})