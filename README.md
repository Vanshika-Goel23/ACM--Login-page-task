# ACM--Login-page-task
This program deals with the login Authentication page of a Shopping site. This works as per the django framefork which is based on python.
The templates are HTML5 based and stylig is done using css and bootstrap. 
The program generates a Register form which is an inbuilt feature of django and allows user to register himself/herself as a user who can Login
The django recieves the data and stores it into it's in-built database 'db.sqlite3'. The user is thus requires to provide a username, Email(not compulsory), Password,Confirm password and DOB.
This data is stored in User model of django which is again an in-built feature of django.
Although it doesn't provide fields of email and DOB, but these can be created easily using meta class
Now after signing up, the user is redirected to LOGIN page, which again is an in-built feature of django, so we need to just import it to our urls file
After this, the user name and password needs to be entered by the user and he can login into the website.and thus can see his own profile
Also the admin page which can only be accessed by superuser.


Some glimpses of our task:
https://user-images.githubusercontent.com/82586051/115699705-873e9180-a383-11eb-964e-323a87f5f706.jpeg
https://user-images.githubusercontent.com/82586051/115699729-8d347280-a383-11eb-9e6d-d1b55046cded.jpeg
