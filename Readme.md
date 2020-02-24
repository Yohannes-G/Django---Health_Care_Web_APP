 HomePageView
 
# Requirements                                                   
1.Django - To install django type 'pip install django' in cmd.                             
2.PASSWORD HASHERS - To   'pip install  django[Argon2]' in cmd.                       
3. PASSWORD HASHERS - To install allAuth type 'pip install bycrypt' in cmd.                                        
4.for image uploading 'pip install pillow'

To run the server follow the given steps below:                                 
1. Open CMD in the forked local directory where manage.py file is located.                             
2. Type 'python manage.py makemigrations' and hit enter to create track of migrations.                        
3. Type 'python manage.py migrate' and hit enter to migrate the tracked files.                    
4. Type 'python manage.py runserver' and hit enter to run the server.                        
5. While the server is running, navigate to your favourite browser and navigate to 'localhost:8000' to view the webapp.                          

If you want to make a new admin id just hit following command - 
'python manage.py createsuperuser'
Then provide the asked information and you are all set up!

