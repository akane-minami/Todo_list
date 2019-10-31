from django.db import models

# Create your models here.

class Todo(models.Model):#フィールド:各クラスの属性を表す
    todo=models.CharField('ToDo',max_length=100,blank=False)#文字フィールド
    created_at=models.DateTimeField('作成日時',auto_now_add=True)#日付と時刻のフィールド
    updated_at=models.DateTimeField('更新日時',auto_now=True)

    def _str_(self):
        return self.todo