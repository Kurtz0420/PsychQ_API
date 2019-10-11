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

URL's
======

+ '/admin' - admin panels func : all control
+ 'api/psychq/posts/ - will list the items in the database as well as ability to post new item
+ 'api/psychq/posts/{number} - will return the object of the respective id
+ 'api/psychq/posts/?q={fieldsProvidedIn 'PostApiView.get_query} - searches the title/data inside items
+ 'api/psychq/categories

Query
=======

+ Api can be queried by the following fields
    -id
    -title
    -category
    -universal_count

POSTS REQUESTS
=========

+ GET - /api/psychq/posts
        will retrieve all the objects of posts

+ GET - /api/psychq/posts/?q={title/category/id}
        will retrieve posts associated with title/category/id

+ GET - /api/psychq/posts/{id}
        will retrieve posts associated with that id

+ POST - /api/psychq/posts/
            -title
            -category
            -sub_category
            -storage_link
            -universal_count
            -category_count
            -sub_post_count
            -description
            -is_printable
            -tags
            -views
            -downloads
            -id {generated automatically with POST}
            -timestamp {generated Auto}
        will post object if model is valid

+ PUT - /api/psychq/posts/{id {post_id}}
        will replace the object related to that id/pk

+ PATCH - /api/psychq/posts/{id}
        can update individual properties of an object
        as well as the whole object related t0 that id


CATEGORIES REQUESTS
=========

+ GET - /api/psychq/categories
        will retrieve all the objects of categories in psychQ

+ GET - /api/psychq/categories/{pk of category}
        will retrieve category of associated pk in psychQ

+ GET - /api/psychq/categories/?q={code or title}
        will retrieve category of associated code or title in psychQ

+ POST - /api/psychq/categories/
        will post object if model is valid

+ PUT - /api/psychq/categories/{id or pk}
        will replace the object related to that id/pk

+ PATCH - /api/psychq/categories/{id/pk}
        can update individual properties of an object
        as well as the whole object related t0 that id


ORDERS REQUESTS
=========

+ GET - /api/psychq/orders
        will retrieve all the objects of orders

+ GET - /api/psychq/orders/{pk}
        will retrieve object related to that pk

+ GET - /api/psychq/orders/?={user_id/product_id/order_id}
        will query orders by user_id/product_id {howMuchSaleOfIndividualProduct}/
        order_id {trackAnOrderByItsID}

+ POST - /api/psychq/orders/
        will post object if model is valid

+ PUT - /api/psychq/orders/{post id or pk}
        will replace the object related to that id/pk

+ PATCH - /api/psychq/orders/{pk/order_id}
        can update individual properties of an object
        as well as the whole object related t0 that id


REVIEWS REQUESTS
=========

+ GET - /api/psychq/reviews
        will retrieve all the objects

+ GET - /api/psychq/reviews/{pk}
        will retrieve object associated with pk

+ GET - /api/psychq/reviews/?q={user_id/product_id}
        will retrieve all instances of
        - user_id {howMuchReviewsHaveUserMadeOnHowManyProducts}
        - product_id {howMuchReviewsAreAssociatedWithASingleProduct}

+ GET - /api/psychq/reviews/?q={clean_id}
        will retrieve the unique review by its id {clean}

+ GET - /api/psychq/reviews/{id}
        will retrieve the unique review by its id

+ POST - /api/psychq/reviews/
            -title
            -description
            -user_id
            -product_id
        will post object if model is valid

+ PUT - /api/psychq/{id}/  SLASH AT THE END
            -title
            -description
        will replace the object related to that id/pk

+ PATCH - /api/psychq/reviews/{id {review_id to be precise}}/  SLASH AT THE END
            -title
            -description
        can update individual properties of an object
        as well as the whole object related t0 that id