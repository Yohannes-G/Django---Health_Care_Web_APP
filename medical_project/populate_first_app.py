import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_project.settings')

import django
django.setup()


#fake pop script
import random
from hospital_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social', 'Marketplace', 'News','Games']

def add_topic():
    t  = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        
        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        
        #create fake date for user
        fake_name1 = fakegen.name().split()
        fake_first_name = fake_name1[0]
        fake_last_name = fake_name1[1]
        fake_email = fakegen.email()
        
        #new entry for user
        user = User.objects.get_or_create( 
                                           first_name=fake_first_name,
                                           last_name=fake_last_name,
                                           email=fake_email
                                        )[0]
        
        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        
        #create a fake access records for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        
if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
        