import os
import csv
from io import StringIO
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

#from corecode.models import StudentClass
from .models import CustomUser, StaffBulkUpload, Staffs

@receiver(post_save, sender=StaffBulkUpload)
def create_bulk_staff(sender, created, instance, *args, **kwargs):

    if created:
        opened = StringIO(instance.csv_file.read().decode())
        reading = csv.DictReader(opened, delimiter=',')
        staffs = []
        users= []
        for row in reading:
            if 'username' in row and row['username']:
                username     = row['username'] 
                first_name   = row['first_name'] if 'first_name' in row and row['first_name'] else ''
                last_name    = row['last_name'] if 'last_name' in row and row['last_name'] else ''
                email        = row['email'] if 'email' in row and row['email'] else ''
                password     = row['password'] if 'password' in row and row['password'] else ''
                

                check = CustomUser.objects.filter(username=username).exists()
                if not check:
                    users.append(
                        CustomUser(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            user_type=2,
                            password=make_password(password)
                        )
                    )

        for row in reading:
            if 'staff_number' in row and row['staff_number']:
                staff_number = row['staff_number'] 
                address      = row['address'] if 'address' in row and row['address'] else ''
                dob          = row['dob'] if 'dob' in row and row['dob'] else ''
                gender       = (row['gender']).lower() if 'gender' in row and row['gender'] else ''
                 
                staffs.append(
                    Staffs(
                        staff_number=staff_number,
                        gender=gender,
                        address=address,
                        dob=dob,
                    )
                )
               
        Staffs.objects.bulk_create(staffs)
        CustomUser.objects.bulk_create(users)
        instance.csv_file.close()
        instance.delete()


def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

@receiver(post_delete, sender=StaffBulkUpload)
def delete_csv_file(sender, instance, *args, **kwargs):
    if instance.csv_file:
        _delete_file(instance.csv_file.path)


@receiver(post_delete, sender=Staffs)
def delete_passport_on_delete(sender, instance, *args, **kwargs):
    if instance.passport:
        _delete_file(instance.passport.path)
