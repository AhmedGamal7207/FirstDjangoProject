
# Creating Virtual Environment

Go to the folder you want to create the project in then run this in CMD
```cmd
virtualenv env
```

then change direction to the virtual environment you just created
```cmd
cd env
```

run(activate) the virtual environment
```cmd
.\Scripts\activate
```

Install Django
```cmd
python -m pip install django
```

---
# Creating My Project

Run this line to create the project
```cmd
django-admin startproject FirstProject
```

Go the FirstProject directory
```cmd
cd FirstProject
```

Run this line to create a new Application
```cmd
python manage.py startapp FirstApp
```

---
# Creating Admin User (superuser)

Run this line to start creating the super user
```cmd
python manage.py createsuperuser
```

---
# Running and Loading the Server

First, Make migrations
```cmd
python manage.py makemigrations
```

Then, Migrate
```
python manage.py migrate
```

Running the server
```cmd
python manage.py runserver
```

NOTE: if you want your server to be locally published on your network, add your Local IP Address and a port to the previous line
```cmd
python manage.py runserver 192.168.1.155:8080
```

But you must edit this line in FirstPorject.settings.py
```py
ALLOWED_HOSTS = ['*'] # add the '*' inside the list
```

To get your Local IP Address, you can run:
```cmd
ipconfig
```
![[Pasted image 20240826001846.png]]

You can also migrate the sqlite3 changes by using this line:
```cmd
python manage.py sqlmigrate FirstApp 0001
```

---
# First Configurations

You should open the First Project Main Folder with VS Code

## Create your first model

Go to FirstApp.models.py file
```py
from django.db import models

# Create your models here.

class Post(models.Model):
    # Here we add our fields
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    text = models.TextField()

    # To have titles appear in the table in admin page
    def __str__(self):
        return self.title
```

## Register that new model in admin

Go to FirstApp.admin.py
```py
from django.contrib import admin
from FirstApp.models import Post

# Register your models here.
admin.site.register(Post)
```

Edit this in FirstProject.settings.py
```cmd
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'FirstApp.apps.FirstAppConfig' # Add this
]
```

## Create the templates (HTML Files)

First, Create a folder named templates inside the FirstApp folder and add the HTML File
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Home Page</h1>
    </body>
</html>
```

Second, Edit the DIRS key in TEMPLATES dictationary inside FirstProject.settings.py 
```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'FirstApp/templates')], # I edited this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## Create a view for the template

Go to FirstApp.views.py and add a Class for that template you just created
```py
from django.views.generic import TemplateView,ListView
class MyHome(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'
```

You can add manual context to the class (not from the Post model) by overriding
```py
class MyHome(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts'
    def get_context_data(self):
        context = {
        'items':["First","Second","Third"]
        }
        return context
```

Or you can create a function for the template (not a class) (better)
```py
def my_home(request):
    context = {
        'items':["First","Second","Third"]
    }
    return render(request,'home.html',context)
```

## Configure the URLs to load specific views

First, create file named urls.py inside the FirstApp Folder and add this code
```py
from django.contrib import admin
from django.urls import path
from FirstApp.views import MyHome

urlpatterns = [
    path('home/', MyHome.as_view(), name="home"),
    path('', MyHome.as_view(), name="home"),
    path('about/', MyAbout, name="about"),
]
```

Then, go to FirstProject.urls.py and modify its code to be:
```py
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('FirstApp.urls'))
]
```

## Create a base in HTML (header menu)

First, create the base (header) html file
```html
<body>
    <a href= "{% url 'home' %}">Home</a>
    <a href= "{% url 'about' %}">About</a>
    
    {% block content %}
    {% endblock content %}
</body>
```

Then modify the home and about pages to put all body code inside the block content and start the body with extends line
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        {% extends 'header.html' %}
        
        {% block content %}
        <h1>Home Page</h1>
        {% endblock content %}
    </body>
</html>
```

---
# Pass data from model through view to template

If you are using a Class as view, you will edit your html file to this
```html
<body>
        {% extends 'header.html' %}

        {% block content %}

        <h1>Home Page</h1>
        <hr>

        {% for i in all_posts %}
        <h2>{{i.title}}</h2>
        <h4>{{i.author}}</h4>
        <p>{{i.text}}</p>
        <hr>
        {% endfor %}
        
        {% endblock content %}
    </body>
```

OR if you are using a function as view, you will edit your function to be: (better)
```py
def MyHome(request):
    context = {
        'all_posts': Post.objects.all()
    }
    return render(request, 'home.html',context)
```
along with the same html code attached above this cell

---
# Add Foreign Key

Edit your model
```py
class Post(models.Model):
    # Edit the field you want to have the foreign key
    author = models.ForeignKey(
        'auth.User',

        on_delete = models.CASCADE

    )

```

If there is an error because of the foreign key , you can delete the sqlite3.db file located in the FirstProject main folder then run this command in CMD
```cmd
python manage.py sqlmigrate FirstApp 0001
```

---
# Running my Project again

- Go to the env path and run Activate
- Then change direction to FirstProject Main Folder then runserver

