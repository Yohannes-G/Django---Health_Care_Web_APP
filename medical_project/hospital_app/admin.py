from django.contrib import admin
from hospital_app.models import AccessRecord,Patient_information, Topic, Webpage, User_profile, Hospital_list,Appointment_date,UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User_profile)
admin.site.register(Hospital_list)
admin.site.register(Appointment_date)
admin.site.register(Patient_information)
admin.site.register(UserProfileInfo)
 