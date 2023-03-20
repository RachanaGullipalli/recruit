from django.db import models

class recruiter(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self):
        return self.username
    
class student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username
    
class jobs(models.Model):
    connect = models.CharField(max_length=50)
    job_tittle  = models.CharField(max_length=50)
    company  = models.CharField(max_length=50)
    job_type  = models.CharField(max_length=50)
    Location  = models.CharField(max_length=50)
    job_description  = models.CharField(max_length=50)

