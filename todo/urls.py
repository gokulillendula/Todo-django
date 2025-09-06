from django.urls import path
from . import views
urlpatterns=[
    #adding a task
    path('addTask/',views.addTask,name='addTask'),
    #marking a task as done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    #deleting a task
    path('delete/<int:pk>/',views.delete,name='delete'),
    #marking a task as undone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    #editing a task
    path('edit_task/<int:pk>',views.edit_task,name='edit_task')
]