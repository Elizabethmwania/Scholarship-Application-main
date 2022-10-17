from django.db import models

# Create your models here.
class SponsoredApplications(models.Model):
    firstName= models.CharField(max_length=100)
    lastName=  models.CharField(max_length=100)
    homeAddress = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    idFile = models.FileField(upload_to='Documents', blank=True)
    certFile= models.FileField(upload_to='Documents', blank=True)
    schoolName= models.CharField(max_length=100)
    schoolAddress= models.CharField(max_length=100)
    academicLevel = models.CharField(max_length=100)
    completionYear = models.IntegerField()
    reason = models.TextField()
    status =models.CharField(default = "Pending", max_length = 100)
    sponsorName = models.CharField(max_length=100)
    sponsorPhoneNumber = models.IntegerField()
    
class Meta:
    # Add verbose name
    verbose_name = 'Sponsored Applications'


