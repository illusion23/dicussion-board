from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Board
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
    pass