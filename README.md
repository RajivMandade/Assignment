# Assignment
Solved assignment for entering  records and displaying it without using database. I store the data in list and then displayed it by extracting data from list by applying for loop
Procedure:
1. Create project folder by putting command in prompt: django-admin startproject Assignment
2. Then create app for it : python manage.py startapp fapp
3. Then mention app name in settings.py file whicb is present in Project folder
4. Then mention the app urls in Project folder file having name urls.py
5. Then mention urls of templates  in app folder having simlilar name urls.py by which we can navigate on different pages and also go on  respective function present in views.py
6. Now open views.py create function for displaying data,entering data,deleting data.
7. Also create variable with list at top of views.py
8. Retrieve data from html file using post method and add it into list by using append.
9. Display store data in the list by appying while loop on html page using json format.
