from audioop import reverse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from .models import JOB_TYPE, Job
from .forms import ApplyForm,Jobform
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.

def jop_list(request):
    job_list=Job.objects.all()
    myfilter=JobFilter(request.GET,queryset=job_list)
    job_list=myfilter.qs
    paginator = Paginator( job_list, 3) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={'jobs':page_obj ,'myfilter': myfilter}
    return render(request,'job/job_list.html',context)

def jop_detail(request,slug):
    jop_detail=Job.objects.get(slug=slug)
    if request.method == 'POST':
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=jop_detail
            myform.save()
            
            
    else:
        form=ApplyForm()
    context={
        'form1':form,
        'job':jop_detail
        
        }
    return render(request,'job/job_detils.html',context)

@login_required
def add_job(request):

    if request.method=='POST':
        form=Jobform(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect('jobs:job_list')


            
    else:
        form=Jobform()
        
    context = {
            
        'form1':form
         
        }
    
    return render(request,'job/add_job.html',context)