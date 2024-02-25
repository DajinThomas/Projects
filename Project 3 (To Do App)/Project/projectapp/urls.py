from django.urls import path
from .views import task_db, task_delete, task_update,TaskCreateView,TaskDetailView,TaskListView, TaskUpdateView, TaskDeleteView
urlpatterns = [
    # Using function views
    path('', task_db, name='task_db'),
    path('task_delete/<int:id>/', task_delete, name='task_delete'),
    path('task_update/<int:id>/', task_update, name='task_update'),
    path('task/<int:id>/update/', task_update, name='task_update'),

    # Using class views
    # path('index/', index.as_view(), name='index'),
    path('index/', TaskCreateView.as_view(), name='task_create'), # for adding Task
    path('index_detail/<int:pk>/', TaskDetailView.as_view(), name='index_detail'),  # For pick individual task
    path('tasks/', TaskListView.as_view(), name='task_list'), # for Getting all task in collectively
    path('index_detail/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'), # For Updating existing task
    path('index_detail/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'), # for deleting a existing task
]