from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator


#Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
    user_type      = models.CharField(default=1, choices=user_type_data, max_length=10)



class AdminHOD(models.Model):
    id         = models.AutoField(primary_key=True)
    admin      = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects    = models.Manager()



class Staffs(models.Model):
    id           = models.AutoField(primary_key=True)
    admin        = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address      = models.TextField()
    num_regex    = RegexValidator(regex="^[0-9]{10,15}$", message="Example: 17882282")
    staff_number = models.CharField(validators=[num_regex], max_length=13, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    gender       = models.CharField(max_length=10)
    updated_at   = models.DateTimeField(auto_now=True)
    dob          = models.DateField(default=timezone.now)
    profile_pic  = models.FileField(blank=True)
    objects      = models.Manager()

    def date_of_birth(self):
        return self.dob.strftime('%D-%M-%Y')

class StaffBulkUpload(models.Model):
    date_uploaded = models.DateTimeField(auto_now=True)
    csv_file      = models.FileField(upload_to='staffs/bulkupload/')



class Students(models.Model):
    id              = models.AutoField(primary_key=True)
    admin           = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender          = models.CharField(max_length=10)
    profile_pic     = models.FileField()
    address         = models.TextField()
    course_id       = models.ForeignKey('Courses', on_delete=models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey('SessionYearModel', on_delete=models.CASCADE)
    num_regex       = RegexValidator(regex="^[0-9]{10,15}$", message="Example: 17882282")
    parent_number   = models.CharField(validators=[num_regex], max_length=13, blank=True)
    dob             = models.DateField(default=timezone.now)
    #current_class   = models.CharField('Courses')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    objects         = models.Manager()






class SessionYearModel(models.Model):
    id                 = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year   = models.DateField()
    objects            = models.Manager()

    def start_year(self):
        return self.session_start_year.strftime('%Y')
    
    def end_year(self):
        return self.session_end_year.strftime('%Y')


class Courses(models.Model):
    id          = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    objects     = models.Manager()

    def __str__(self):
	    return self.course_name



class Subjects(models.Model):
    id           =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id    = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1) #need to give defauult course
    staff_id     = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    objects      = models.Manager()





class Attendance(models.Model):
    id              = models.AutoField(primary_key=True)
    subject_id      = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    objects         = models.Manager()


class AttendanceReport(models.Model):
    # Individual Student Attendance
    id            = models.AutoField(primary_key=True)
    student_id    = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status        = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    objects       = models.Manager()


class LeaveReportStudent(models.Model):
    id            = models.AutoField(primary_key=True)
    student_id    = models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date    = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status  = models.IntegerField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    objects       = models.Manager()


class LeaveReportStaff(models.Model):
    id            = models.AutoField(primary_key=True)
    staff_id      = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date    = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status  = models.IntegerField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)
    objects       = models.Manager()


class FeedBackStudent(models.Model):
    id             = models.AutoField(primary_key=True)
    student_id     = models.ForeignKey(Students, on_delete=models.CASCADE)
    feedback       = models.TextField()
    feedback_reply = models.TextField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    objects        = models.Manager()


class FeedBackStaffs(models.Model):
    id             = models.AutoField(primary_key=True)
    staff_id       = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    feedback       = models.TextField()
    feedback_reply = models.TextField()
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
    objects        = models.Manager()



class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class NotificationStaffs(models.Model):
    id         = models.AutoField(primary_key=True)
    stafff_id  = models.ForeignKey(Staffs, on_delete=models.CASCADE)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects    = models.Manager()


class StudentResult(models.Model):
    id                       = models.AutoField(primary_key=True)
    student_id               = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id               = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    subject_exam_marks       = models.FloatField(default=0)
    subject_assignment_marks = models.FloatField(default=0)
    created_at               = models.DateTimeField(auto_now_add=True)
    updated_at               = models.DateTimeField(auto_now=True)
    objects                  = models.Manager()


""" Creating Django Signals
It's like trigger in database. 
It will run only when Data is Added in CustomUser model """

@receiver(post_save, sender=CustomUser)
# Now Creating a Function which will automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    
    if created:      # if Created is true (Means Data Inserted)
                     # Check the user_type and insert the data in respective tables
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staffs.objects.create(admin=instance)
        if instance.user_type == 3:
            Students.objects.create(
                admin=instance, 
                course_id=Courses.objects.get(id=1), 
                session_year_id=SessionYearModel.objects.get(id=1), 
                address="", 
                profile_pic="", 
                gender=""
            )
    

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staffs.save()
    if instance.user_type == 3:
        instance.students.save()
    


