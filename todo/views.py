from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList

def todo(request):
    
    if request.method == "POST":
        

        if "add_task" in request.POST:
            title = request.POST.get("title")
            if title:
                TodoList.objects.create(title=title, done = 0)
            return redirect('todo')
        
        if 'edit_task' in request.POST:
            task_id = request.POST.get('task_id')
            new_title = request.POST.get('new_title')
            task = get_object_or_404(TodoList, id = task_id)
            task.title = new_title
            task.save()
            return redirect('todo')
        
        if 'done_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(TodoList, id = task_id)
            if task.done:
                task.done = False
            else: task.done = True
            task.save()
            return redirect('todo')
        

        if 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = get_object_or_404(TodoList, id = task_id)
            task.delete()
            return redirect('todo')
        
        if 'clear_all' in request.POST:
            TodoList().objects.all().delete()
            return redirect('todo')
        
        
    if "all_task" in request.POST:
        todos = TodoList.objects.all()
        
        
    elif "complited_task" in request.POST:
        todos = TodoList.objects.filter(done = 1)
        
    else:
        todos = TodoList.objects.filter(done = 0)
        
        




    
    return render(request, 'todo.html', {"todos":todos, "task_count": todos.count()})
