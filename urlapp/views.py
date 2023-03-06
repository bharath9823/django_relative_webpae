from django.shortcuts import render

# Create your views here.
def index(request):
    mydict={'insert_me':'i am the devil of my world'}
    return render(request,'index.html',context=mydict)
def contact(request):
    mydict={'insert_me':'i am the devil of my world'}
    return render(request,'contact.html',context=mydict)
def relative(request):
    mydict={'insert_me':'i am the devil of my world'}
    return render(request,'relative.html',context=mydict)
def about(request):
    mydict={'insert_me':'i am the devil of my world'}
    return render(request,'about.html',context=mydict)