PsychQ Api
===========.

Setting Up Project in Pycharm:
install python 3.7
setup interpreter
create a virtual environment

then install the following in interpreter :
pip install Markdown
pip install django-filters
pip install Django
pip install sqlparse
pip install djangorestframework


then sync the database
install adbc by going into database on side panel
python manage.py makemigrations
python manage.py migrate

+ This api contains four apps
    -posts
    -categories
    -merch
    -shopping

 '/admin' - admin panels func : all control
 'api/psychq/posts/ - will list the items in the database as well as ability to post new item
 'api/psychq/posts/{number} - will return the object of the respective id
 'api/psychq/posts/?q={fieldsProvidedIn 'PostApiView.get_query} - searches the title/data inside items

Query
=======

+ Api can be queried by the following fields
    -id
    -title
    -category
    -universal_count

REQUESTS
=========

+ GET - /api/psychq/posts
        will retrieve all the objects of posts in psychQ

+ POST - /api/psychq/posts/
        will post object if model is valid

+ PUT - /api/psychq/posts/{post id or pk}
        will replace the object related to that id/pk

+ PATCH - /api/psychq/posts/{id/pk}
        can update individual properties of an object
        as well as the whole object related t0 that id