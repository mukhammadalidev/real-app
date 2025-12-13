from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.views import View
from advertisement.models import CategoryModel,Job
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


class IndexView(View):
    def get(self,request):


        category = CategoryModel.objects.all()
        latest_jobs = Job.objects.all().order_by('-created_at')[:9]

        print(latest_jobs.first().employer.logo)
        return render(request,'index.html',context={"categories":category,"latest_jobs":latest_jobs})
    

def search(request):
    query = request.GET.get("q","")
    result = Job.objects.filter(Q(title__icontains=query)) | Job.objects.filter(Q(description__icontains=query))
    print(result)
    return render(
        request,
        "index.html",
        {
            "latest_jobs":result
        }
    )





class SearchView(View):
    def get(self, request):
        query = request.GET.get("q", "")

        jobs = Job.objects.all()

        if query:
            jobs = jobs.filter(title__icontains=query) | jobs.filter(description__icontains=query)

        context = {
            "query": query,
            "jobs": jobs
        }
        return render(request, "category/search.html", context)
    

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # Bu yerda siz xabarni saqlashingiz yoki email yuborishingiz mumkin
        messages.success(request, "Xabaringiz yuborildi, rahmat!")
        return redirect("contact")
    return render(request, "contact.html")


def about_view(request):
    return render(request,'pages/about.html')

def faq_view(request):
    return render(request,'pages/faq.html')




class JobRemove(View):
    def post(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        job.delete()
        messages.success(request, "Ish muvaffaqiyatli o‘chirildi.")
        return redirect('search')