from django.shortcuts import render, redirect
from .models import Movie
from . forms import MovieForm

# Create your views here.
def home(request):
    context={
        'obj': Movie.objects.all(),
    }


    return render(request,'home.html',context)

def detailse(request,id):
    obj=Movie.objects.get(id=id)
    return render(request,'detalis.html',{'obj':obj})


def add(request):
    if request.method=='POST':
        name=request.POST['name']
        desc=request.POST['desc']
        img=request.FILES['img']
        year=request.POST['year']
        movie=Movie(name=name,desc=desc,img=img,year=year)
        movie.save()
        return redirect('/')

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
