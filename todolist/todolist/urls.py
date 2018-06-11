from django.contrib import admin
from django.urls import path
from tasks.views import (
    Index,
    Categories,
    AddCategory,
    EditCategory,
    DeleteCategory,
    AddTask,
    Tasks,
    EditTask,
    DeleteTask
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('categories/', Categories.as_view(), name='categories-list'),
    path('add_category/', AddCategory.as_view(), name='add-category'),
    path('edit_category/<int:category_id>', EditCategory.as_view(), name='edit-category'),
    path('delete_category/<int:category_id>', DeleteCategory.as_view(), name='delete-category'),
    path('tasks/', Tasks.as_view(), name='tasks'),
    path('add_task/', AddTask.as_view(), name='add-task'),
    path('edit_task/<int:task_id>', EditTask.as_view(), name='edit-task'),
    path('delete_task/<int:task_id>', DeleteTask.as_view(), name='delete-task'),
]