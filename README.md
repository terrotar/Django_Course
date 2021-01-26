
*************************************************************************************************

Here you will found my personal summary of some tips and hints that I think it's interesting for a fast checkout if necessary.

*************************************************************************************************

    SUMMARY


* `django-admin startproject mysite` // That's the first command to create mysite folder in your
project directory

* `python manage.py runserver` // Start the development enviroment in a browser

* `python manage.py migrate` // Some kind of commit of the database schema. Creates the database schema(default=SQLite)
in the file 'db.sqlite3'. You can modify the tables, columns and realationship in the file 'polls/models.py'.

* `python manage.py makemigrations polls` // Basically it say to Django that you made some changes
to your models and store it in migrations. Django store these changes of models in 'migrations/0001_initial.py'
for the first time and so on, in case you need to edit or something.

* `python manage.py sqlmigrate polls number_of_your_migration(first=0001)` // A command that will run the migrations
for you and manage your database schema automatically. It literally format the 'polls/models.py' in to your database
of choice(default=SQLite).

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

* `path('', views.index, name='index')` 

                                        // '' = The route text, for example 'user/home'. When it's
                                        empty means literally the webpage, in that case, 'localhost/polls'. Notice that '/polls' is linked
                                        by a path in 'mysite/urls.py' which load the URL's patterns of folder polls

                                        // views.index = Function index inside views files

                                        // name = It's a shortcut name to make it easier to find the
                                        route instead of type it all the way down.

* `Models changes` // To do so, first you need to change your models in 'polls/models.py'. Then, run the command
'python manage.py makemigrations polls' to save those changes in the folder 'polls/migrations'. Finally, you run
the command 'python manage.py migrate' to apply those changes to the database.

* `migrations` // Migrations are basically saves of the changes you've made in your models of database schema. The
folder will save all 'python manage.py makemigrations polls' commands the project has done, smoothing the manage
and control of database versions.

* `Configuration of INSTALLED_APPS in file 'mysite/settings.py'` // Imagine that you downloaded a program but
you didn't install it. If you create a database schema for example, you need to "load" that app. For that, you need
to include 'polls.apps.PollsConfig' in the list.

* `Change timezone` // Just put your local file in timezone pattern of 'mysite/settings.py', for example 'America/Sao_Paulo'.

* `About 'polls/views.py'` // All that Django accept as return is a 'return HttpResponse()' or raise an exception for an error,
like 404. With the first option, you can do pratically anything, link a PDF, or a template.

* `How Django search files/pastes` // Now we might be able to get away with putting our templates directly in polls/templates (rather than creating another polls subdirectory), but it would actually be a bad idea. Django will choose the first template it finds whose name matches, and if you had a template with the same name in a different application, Django would be unable to distinguish between them. We need to be able to point Django at the right one, and the best way to ensure this is by namespacing them. That is, by putting those templates inside another directory named for the application itself.

* `Namespacing URL names` // In Django, it's normal to have some app's, and some of them has a name of a path(for example, name=detail, or name=index) that it's the same of another app, like index of the website and index of an android app. To solve that problem, you can
first of all create an APP_NAME in your URL_PATTERN. Doing so, you will be able to summon the path in your templates like the follow example: <a href="{% url 'polls:index' %}"></a>

* `csrf_token in templates` // In any template that uses a POST form, use the csrf_token tag inside the <form> element if the form is for an internal URL. That's a safe and simple way to prevent CSRF(Cross Site Request Forgeries) attacks.
