from django.views import View
from .models import Job,Application,Worker
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .forms import AdsEmployer,ApplicationForm,WorkerForm
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
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
        workers = Worker.objects.all().order_by('-created_at')
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
    




from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job, CategoryModel, EmployerProfile
from rest_framework.permissions import AllowAny


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Job, EmployerProfile, CategoryModel
import re

@method_decorator(csrf_exempt, name='dispatch')
class ChannelView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        text = request.data.get("text")
        if not text:
            return Response({"error": "Text yo‘q"}, status=400)

        # --- DATA EXTRACT ---
        # Sarlavha
        title_match = re.search(r"Sarlavha:\s*(.*)", text, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else "No Title"

        # Kategoriya
        category_match = re.search(r"Kategoriya:\s*(.*)", text, re.IGNORECASE)
        category_name = category_match.group(1).strip() if category_match else ""

        # Manzil
        location_match = re.search(r"Manzil:\s*(.*)", text, re.IGNORECASE)
        location = location_match.group(1).strip() if location_match else "No Location"

        # Maosh
        salary_match = re.search(r"Maosh[:\s]*(.*)", text, re.IGNORECASE)
        salary = salary_match.group(1).strip() if salary_match else "Kelishiladi"

        # Telefon
        phone_match = re.search(r"Telefon[:\s]*(.*)", text, re.IGNORECASE)
        if not phone_match:
            # Ba’zida boshqa format
            phone_match = re.search(r"\d{2,4}-\d{2,3}-\d{2,3}", text)
        phone_number = phone_match.group(0).strip() if phone_match else "No Phone"

        # Tasnif
        tasnif_match = re.search(r"Tasnif:(.*)", text, re.IGNORECASE | re.DOTALL)
        description = tasnif_match.group(1).strip() if tasnif_match else text

        # --- CATEGORY ---
        category = CategoryModel.objects.filter(title__icontains=category_name).first()
        if not category:
            category = CategoryModel.objects.first()  # default

        # --- EMPLOYER ---
        employer = EmployerProfile.objects.first()  # TEST

        # --- CREATE JOB ---
        job = Job.objects.create(
            employer=employer,
            category=category,
            title=title,
            location=location,
            salary=salary,
            phone_number=phone_number,
            description=description
        )

        return Response({"status": "created", "job_id": job.id}, status=201)

