from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.order_by("due_date").all()
    
    return render(request,"todo/index.html",{"todos":todos})

def new(request):
    return render(request,"todo/new.html")
    
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due_date")
    
    # Todo.objects.create(title=title,content=content,due_date=due_date) #아래 두줄을 간편하게 사용할수있다. 생성과저장
    todo = Todo(title=title,content=content,due_date=due_date)
    todo.save()

    return redirect("/todos")
    
def read(request,id):
    todo = Todo.objects.get(pk=id)
    
    return render(request,"todo/read.html",{"todo":todo})
    
def delete(request,id): #글을 지우는 함수
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect("/todos")
    
def edit(request,id):
    todo = Todo.objects.get(pk=id)
    return render(request,"todo/edit.html",{"todo":todo})

def update(request,id):
    todo = Todo.objects.get(pk=id)
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    due_date = request.POST.get("due_date")
    
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()
    
    return redirect(f"/todos/{id}/")
    