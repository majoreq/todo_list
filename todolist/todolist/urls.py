from django.contrib import admin
from django.urls import path
from tasks.views import index, categories, add_category, edit_category, delete_category, add_task, tasks, edit_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.as_view(), name='index'),
    path('categories/', categories.as_view(), name='categories-list'),
    path('add_category/', add_category.as_view(), name='add-category'),
    path('edit_category/<int:category_id>', edit_category.as_view(), name='edit-category'),
    path('delete_category/<int:category_id>', delete_category.as_view(), name='delete-category'),
    path('tasks/', tasks.as_view(), name='tasks'),
    path('add_task/', add_task.as_view(), name='add-task'),
    path('edit_task/<int:task_id>', edit_task.as_view(), name='edit-task'),
    path('delete_task/<int:task_id>', delete_task.as_view(), name='delete-task'),

]

