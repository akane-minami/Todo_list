#from django.shortcuts import render
#Djangoの汎用クラスビューを利用してtodoアプリケーションのビューを作成
from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# Create your views here.
#Todo一覧
class TodoListView(generic.ListView):
    model=Todo
    paginate_by=5

#Todo詳細
class TodoDetailView(generic.DetailView):
    model=Todo

#Todo作成機能
class TodoCreateView(generic.CreateView):
    model=Todo
    form_class=TodoForm
    success_url=reverse_lazy('todo:list')

#Todo編集機能
class TodoUpdateView(generic.UpdateView):
    model=Todo
    form_class=TodoForm
    success_url=reverse_lazy('todo:list')

#Todo削除機能
class TodoDeleteView(generic.DeleteView):
    model=Todo
    success_url=reverse_lazy('todo:list')














