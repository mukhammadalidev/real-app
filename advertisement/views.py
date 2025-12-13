from django.views import View
from .models import Job,Application
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import AdsEmployer,ApplicationForm
class AdvertismentView(View):
    def get(self,request,pk):
        products = Job.objects.filter(category__pk=pk)
      
   
     

        return render(request,'category/category.html',{"products":products})
    
class Job_DetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Job, pk=pk)
        

        return render(request, 'category/job_detail.html', {"product": product})



class AdsEmployerView(View):
    def get(self, request):
        form = AdsEmployer()
        return render(request, 'ads/add.html', {"form": form})

    def post(self, request):
        form = AdsEmployer(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            # Employerni request.user orqali tayinlaymiz
            try:
                ad.employer = request.user.employer
                print(request.user.employer)
            except AttributeError:
                # Agar employer profile yo'q bo'lsa, xatolik yoki redirect
                return redirect('users:profile')  

            ad.save()
            return redirect('home')  # saqlangach, asosiy sahifaga yo'naltirish
        return render(request, 'ads/add.html', {"form": form})
    


class ApplicationView(View):

    def get(self, request, job_pk):
        job = get_object_or_404(Job, pk=job_pk)

        # User allaqachon topshirgan bo‘lsa
        if Application.objects.filter(job=job, applicant=request.user).exists():
            messages.warning(request, 'Siz bu ishga allaqachon topshirgansiz!')
            return redirect('job:job-detail', pk=job.pk)

        form = ApplicationForm()
        return render(request, 'pages/apply.html', {'form': form, 'job': job})


    def post(self, request, job_pk):
        job = get_object_or_404(Job, pk=job_pk)
        form = ApplicationForm(request.POST)

        # User allaqachon topshirganligini yana tekshiramiz
        if Application.objects.filter(job=job, applicant=request.user).exists():
            messages.warning(request, 'Siz bu ishga allaqachon topshirgansiz!')
            return redirect('job-detail', pk=job.pk)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()

            messages.success(request, "Arizangiz ish beruvchiga yuborildi!")
            return redirect('job:job-detail', pk=job.id)

        return render(request, 'pages/apply.html', {'form': form, 'job': job})



