from django.shortcuts import render
from home.models import Works
# Create your views here.
def works(request):
    works_list=Works.objects.all()
    context={
        'works':works_list
    }
    return render(request,'home/index.html',context)
def work_details(request,pk):
    works_list=Works.objects.get(pk=pk)
    context={
        'works':works_list
    }
    return render(request,'home/workdetail.html',context)