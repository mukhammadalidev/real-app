from django.views import View
from .models import Job,Application,Worker
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import AdsEmployer,ApplicationForm,WorkerForm
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
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








class AdvertisementAPIView(APIView):
     def get(self,request,category_pk=None):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class AdvertisementDetailAPIView(APIView):
    def get(self, request, pk):
        job = get_object_or_404(Job, pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
    


class CreateWorker(View):
    def get(self,request):
        form = WorkerForm()
        return render(request,'ads/create_worker.html',{"form":form})
    
    def post(self,request):
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user
            worker.save()
            return redirect('home')
        return render(request,'ads/create_worker.html',{"form":form})
    


class WorkerView(View):
    def get(self,request):
        workers = Worker.objects.filter(status=True)
        print(workers)
        return render(request,'ads/worker_list.html',{"workers":workers})
    

class WorkerDetailView(View):
    def get(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        return render(request, 'ads/worker_detail.html', {"worker": worker})
    
class WorkerDeleteView(View):
    def post(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        worker.delete()
        messages.success(request, "Ishchi e'loni muvaffaqiyatli o'chirildi.")
        return redirect('job:worker_list')
    
class WorkerEditView(View):
    def get(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        form = WorkerForm(instance=worker)
        return render(request, 'ads/edit_worker.html', {"form": form, "worker": worker})

    def post(self, request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            messages.success(request, "Ishchi e'loni muvaffaqiyatli yangilandi.")
            return redirect('job:worker-detail', pk=worker.pk)
        return render(request, 'ads/edit_worker.html', {"form": form, "worker": worker})