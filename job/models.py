from django.db import models

# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

    
class Job(models.Model):
    title=models.CharField(max_length=100)
    job_tybe=models.CharField(max_length=15,choices=JOB_TYPE)
    Description=models.TextField(max_length=10000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experince=models.IntegerField(default=1)
    def __str__(self): 
        return self.title

    

    



    
    
