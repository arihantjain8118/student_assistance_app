from django.db import models
from datetime import date, timedelta



from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
# Create your models here.

class Batch(models.Model):
    course_name = models.CharField(max_length=30)
    course_year = models.IntegerField()
    course_code = models.CharField(max_length=30,unique=True)

    class Meta:
        unique_together = ('course_name','course_year')
    
    def __str__(self):
        return str(self.course_code)

class Lecture(models.Model):
    subject_name = models.CharField(max_length=30)
    faculty_name = models.CharField(max_length=30)
    batch = models.ForeignKey(Batch, on_delete=SET_NULL, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('batch','start_time','end_time')
    
    def clean(self):
        from django.core.exceptions import ValidationError

        found = False # var storing whether any subject is clashing

        for lecture in Lecture.objects.filter(batch=self.batch):
            if (self.start_time > lecture.start_time and self.start_time < lecture.end_time):
                print("1")
                found = True
                break
            if (self.end_time > lecture.start_time and self.end_time < lecture.end_time):
                print("2")
                found = True
                break
            if (self.start_time < lecture.start_time and self.end_time > lecture.end_time):
                print("3")
                found = True
                break
            
        print(found)
        if found:
            raise ValidationError("Overlapping Lectures")
            
        
    def __str__(self):
        return str(self.batch) + ' ' + str(self.subject_name)
