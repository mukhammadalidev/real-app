from django.db import models
from users.models import CustomUser
# Create your models here.
class CategoryModel(models.Model):
    title = models.CharField(max_length=155)
    image = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title
    


class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='employer')
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='employers_logos/',null=True,blank=True)


    def __str__(self):
        return self.company_name

class Job(models.Model):
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE, related_name="jobs")
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE,verbose_name='Kategorya')
    title = models.CharField(max_length=255,verbose_name='Sarlovha')
    description = models.TextField(verbose_name='Tasnif')
    salary = models.CharField(max_length=100, blank=True, null=True,verbose_name='Maosh')
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=155,verbose_name='Manzil')
    phone_number = models.CharField(max_length=14,default='998992606296',verbose_name='Telefon raqam')
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
class AdvertisementModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=155)
    link = models.URLField()
    company = models.CharField(max_length=255,null=True,blank=True)
    job_time = models.CharField(max_length=255,default="9:00 dan 18:00")
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    








class Application(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"
    


class Worker(models.Model):
    full_name = models.CharField(max_length=255,verbose_name='To‘liq ism')
    profession = models.CharField(max_length=255,verbose_name='Kasbi')
    bio = models.TextField(verbose_name='Bio')
    location = models.CharField(max_length=155,verbose_name='Manzil')
    phone_number = models.CharField(max_length=14,verbose_name='Telefon raqam')
    status = models.BooleanField(default=False,verbose_name='Holati')
    salary = models.CharField(max_length=100, blank=True, null=True,verbose_name='Maosh')

    def __str__(self):
        return self.full_name