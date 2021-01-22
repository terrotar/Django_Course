
*************************************************************************************************

    Hey, that's my first project with Django and conda. Trying to get some knowledge and
basic concepts focused in web development.

    Here you will found my personal summary of some tips and hints that I think
it's interesting for a fast checkout if necessary.

*************************************************************************************************

    SUMMARY


* `django-admin startproject mysite` // That's the first command to create mysite folder in your
project directory

* `python manage.py runserver` // Start the development enviroment in a browser

* ``

*************************************************************************************************

    CONCEPTS

* `project VS app` // Apps are similar to a webpage, cellphone app, etc. Projects are the folders
that contains apps

* `'polls/views.py'` // Folder that contains the code that will run when the app is requested, for
example a simple text message

* `mysite/urls.py VS polls/urls.py` // The first is your primary pack of URL patterns. It contains
URL's like admin and polls. Note that inside 'mysite/urls.py' contains a path that connect 'polls/'
to the URL's patterns that are inside 'polls/urls.py'. In other words, it's like a link to another
folder

* `path('', views.index, name='index')` // '' = The route text, for example 'user/home'. When it's
empty means literally the webpage, in that case, 'localhost/polls'. Notice that '/polls' is linked
by a path in 'mysite/urls.py' which load the URL's patterns of folder polls

views.index = Function index inside views files

name = It's a shortcut name to make it easier to find the route instead of type it all the way down.

