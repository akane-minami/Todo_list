from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        exclude=('created_at','updated_at',)#タプル
        #入力項目に作成日時、更新日時は入れない