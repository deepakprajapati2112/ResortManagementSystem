from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("this is utkarsh page")
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
    #return HttpResponse("this is about page")
def service(request):
    return render(request,"service.html")
    #return HttpResponse("this is service page")
def contact(request):
    return render(request,"contact.html")
    #return HttpResponse("this is contact page")
def aboutpayment(request):
    return render(request,"aboutpayment.html")
    #return HttpResponse("this is aboutpayment page")        