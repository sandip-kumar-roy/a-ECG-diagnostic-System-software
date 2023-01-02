from django.shortcuts import render
from search.models import locate_city
# Create your views here.
def search(request):
    context={}
    all_doctors=locate_city.objects.all()
    if "qry" in request.GET:
        q=request.GET["qry"]
        doctors=locate_city.objects.filter(state__icontains=q)
        context['doctors']=doctors
        context['abcd']='search'
    return render(request,'searchresults.html',context)