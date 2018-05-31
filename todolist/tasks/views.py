from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Task
from django.views import View

class index(View):
    def get(self, request):
        return render(request, 'index.html')


class categories(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories.html', {
            'categories': categories
        })



class add_category(View):
    def post(self,request):
        name = request.POST.get('name')
        color = request.POST.get('color')
        if color and name:
            category = Category(
                name=name,
                color=color
            )
            category.save()
            return redirect('categories-list')


    def get(self,request):
        return render(request, 'add_category.html')


class edit_category(View):
    def post(self,request, category_id):
        category = Category.objects.get(id=category_id)
        name = request.POST.get('name')
        color = request.POST.get('color')
        if color and name:
            category.name=name
            category.color=color
            category.save()
        return redirect('categories-list')
    def get(self,request, category_id):
        category = Category.objects.get(id=category_id)
        return render(request, 'edit_category.html', {
            'category':category
        })


class delete_category(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('categories-list')


class tasks(View):
    def get(self, request):
        tasks = Task.objects.all()
        categories = Category.objects.all()
        return render(request, 'tasks.html', {
            'tasks':tasks,
            'categories':categories
        })


class add_task(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'add_task.html', {
            'categories':categories
        })


    def post(self, request):
        category = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        task = Task()
        task.category_id = category
        task.name = name
        task.description = description
        task.save()
        print(task.id)
        print(task.name)
        print(task.description)
        print(task.category)
        return redirect('tasks')


class edit_task(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        categories = Category.objects.all()
        return render(request, 'edit_task.html', {
            'task':task,
            'categories':categories
        })

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        if name and category_id and description:
            task.name = name
            task.description = description
            task.category_id = category_id
            task.save()
        return redirect('tasks')

class delete_task(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('tasks')