from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import todo
from .form import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class taskdetailview(DetailView):
    model=todo
    template_name = 'details.html'
    context_object_name = 'mytask'

class myview(ListView):
    model=todo
    template_name = 'home.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model=todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('dv',kwargs={'pk':self.object.id})
class deletes(DeleteView):
    model=todo
    template_name = 'delete.html'
    success_url=reverse_lazy('view')

# Create your views here.
def myfun(request):
    if request.method == 'POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        data=todo(name=name,priority=priority,date=date)
        data.save()
    task=todo.objects.all()
    return render(request,'home.html',{'task':task})
def delete(request,taskid):
    id=todo.objects.get(id=taskid) #fetching the id from the table todo
    if request.method=='POST':
        id.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=todo.objects.get(id=id)
    form=todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
