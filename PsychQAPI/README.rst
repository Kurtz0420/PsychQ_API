PsychQ Api
===========.

Setting Up Project in Pycharm:
install python 3.7
setup interpreter
create a virtual environment

then install the following in interpreter :
pip3 install Markdown
pip3 install django-filters
pip3 install Django==2.2.6
pip3 install sqlparse
pip3 install djangorestframework
pip3 install django-allauth
pip3 install social-auth-app-django
pip3 install PyJWT
pip3 install certifi
pip3 install chardet
pip3 install defusedxml
pip3 install django-credit-cards
pip3 install django-phone-field
pip3 install uuid

then sync the database
install adbc by going into database on side panel
python manage.py makemigrations
python manage.py migrate

+ This api contains four apps
    -posts = {All the content of psychQ app (Post)}
    -categories = {Categories of above posts}
    -products = {All our products will go here}
    -orders = {Will store all the orders of products}
    -reviews = {Will store all the reviews of users on products}
    -accounts = {Will store all the users}



POSTS REQUESTS
=========

Endpoint for fetching posts

+ GET - /api/psychq/posts/?ordering=custom_ordering
        will retrieve all the objects of posts organized by custom_ordering field (ascending)

+ GET - /api/psychq/posts/?ordering=-custom_ordering
        will retrieve all the objects of posts organized by custom_ordering field (descending)

+ GET - /api/psychq/posts
        will retrieve all the objects of posts

+ GET - /api/psychq/posts/?q=_quotes
        - will retrieve objects posts with matching tags because of '_' sign
        - without '_' sign it will search categories, title, and id's

+ GET - /api/psychq/posts/?q={title/category/id/universal_count}
        will retrieve posts associated with title/category/id

+ GET - /api/psychq/posts/{id}
        will retrieve posts associated with that id

+ POST - /api/psychq/posts/
            -id
            -custom_ordering
            -title
            -description
            -category
            -sub_category
            -thumbnail
            -full_res_image
            -universal_count
            -category_count
            -sub_post_count
            -is_printable
            -tags
            -views
            -downloads
            -shares
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

+ GET - /api/psychq/categories/{id of category}
        will retrieve category of associated id in psychQ

+ GET - /api/psychq/categories/?q={id or title}
        will retrieve category of associated id or title in psychQ

+ POST - /api/psychq/categories/
            -id
            -title
            -description
            -sub_categories {optional}
            -picTop
            -picLeft
            -picRight
            -count_range_from
            -count_range_to
            -tags
            -total_posts_count

        will post object if model is valid

+ PUT - /api/psychq/categories/{id}
        will replace the object related to that id

+ PATCH - /api/psychq/categories/{pk/code}
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
            -product_id
            -user_id
            -country
            -phone_number_with_code
            -full_address
            -state
            -zip_code
            -cc_number
            -cc_expiry
            -cc_code
            -order_status {choices = pending,shipped,completed}

        will post object if model is valid

+ PUT - /api/psychq/orders/{order_id/pk}
                -user_id
                -country
                -phone_number_with_code
                -full_address
                -state
                -zip_code

        will replace the object related to that order_id/pk

+ PATCH - /api/psychq/orders/{pk/order_id}/ SLASH AT THE END
            should only patch the following fields :
                -country
                -phone_number_with_code
                -full_address
                -state
                -zip_code
        can update individual properties of an object
        as well as the whole object related t0 that id


REVIEWS REQUESTS
=========

+ GET - /api/psychq/reviews
        will retrieve all the objects

+ GET - /api/psychq/reviews/{id}
        will retrieve object associated with pk

+ GET - /api/psychq/reviews/?q={user_id/product_id}
        will retrieve all instances of
        - user_id {howMuchReviewsHaveUserMadeOnHowManyProducts}
        - product_id {howMuchReviewsAreAssociatedWithASingleProduct}

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

PRODUCTS REQUESTS
===================


+ GET - /api/psychq/products
        will retrieve all the objects

+ GET - /api/psychq/products/{id}
        will retrieve object associated with id

+ GET - /api/psychq/products/?q={id/product_name}
        will retrieve all instances of matching related field

+ GET - /api/psychq/products/{id}
        will retrieve the unique product by its id

+ POST - /api/psychq/products/
            -id
            -name
            -description
            -quantity_in_stock
            -sales
            -price
            -shipment_charges
            -photos {String of url's separated by a comma}
        will post object if model is valid

+ PUT - /api/psychq/{id}/  SLASH AT THE END
        will replace the object related to that id/pk

+ PATCH - /api/psychq/reviews/{id}/  SLASH AT THE END
        can update individual properties of an object
        as well as the whole object related t0 that id

ACCOUNTS
=========

+Registering a user
- POST - /accounts/register
            -username
            -email
            -password
            -password2


    /accounts/password/reset {gives the option of provide email address and send a link to that email}
    -accounts/signup   {Adds User object}
    -accounts/login    {Authenticate User's object}


-accounts/signup/$ [name='account_signup']
-accounts/login/$ [name='account_login']
-accounts/logout/$ [name='account_logout']
-accounts/password/change/$ [name='account_change_password']
-accounts/password/set/$ [name='account_set_password']
-accounts/inactive/$ [name='account_inactive']
-accounts/email/$ [name='account_email']
-accounts/confirm-email/$ [name='account_email_verification_sent']
-accounts/confirm-email/(?P<key>[-:\w]+)/$ [name='account_confirm_email']
-accounts/password/reset/$ [name='account_reset_password']
-accounts/password/reset/done/$ [name='account_reset_password_done']
-accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
-accounts/password/reset/key/done/$ [name='account_reset_password_from_key_done']
-accounts/social/
-accounts/google/


UNSPLASH CATEGORIES REQUESTS
============================

+ GET - /api/psychq/unsplashcategories
        will retrieve all the objects of categories in psychQ

+ GET - /api/psychq/unsplashcategories/{id of category}
        will retrieve category of associated id in psychQ

+ GET - /api/psychq/unsplashcategories/?q={id or title}
        will retrieve category of associated id or title in psychQ

+ POST - /api/psychq/unsplashcategories/
            -id
            -title
            -description
            -picTop
            -picLeft
            -picRight
            -related_tags
            -total_posts_count

        will post object if model is valid

+ PUT - /api/psychq/unsplashcategories/{id}
        will replace the object related to that id

+ PATCH - /api/psychq/unsplashcategories/{pk/code}
        can update individual properties of an object
        as well as the whole object related t0 that id

CRASH COURSES REQUESTS
============================
-End Point for all the crash courses available (Will Just Display Courses Available)
-Content of the courses can be retrieved from article end point

+ GET - /api/psychq/crashcourses
        will retrieve all the Crash Courses Available in psychQ

+ GET - /api/psychq/crashcourses/{id of Crash Course}
        will retrieve Crash Course of associated id in psychQ

+ GET - /api/psychq/crashcourses/?q={id or title}
        will retrieve Crash Course of associated id or title in psychQ

+ POST - /api/psychq/unsplashcategories/
            -id
            -title
            -description
            -picTop
            -picLeft
            -picRight
            -count_range_from
            -count_range_to
            -first_article_url
            -last_article_url
            -tags
            -total_articles_count

        will post object if model is valid

+ PUT - /api/psychq/crashcourses/{id}
        will replace the object related to that id

+ PATCH - /api/psychq/crashcourses/{pk/code}
        can update individual properties of an object
        as well as the whole object related t0 that id


ARTICLES REQUESTS
=========

+ GET - /api/psychq/articles/?ordering=custom_ordering
        will retrieve all the objects of articles organized by custom_ordering field (ascending)

+ GET - /api/psychq/articles/?ordering=-custom_ordering
        will retrieve all the objects of articles organized by custom_ordering field (descending)

+ GET - /api/psychq/articles
        will retrieve all the objects of articles

+ GET - /api/psychq/articles/?q=_quotes
        - will retrieve objects of articles with matching tags because of '_' sign
        - without '_' sign it will search parent_course, title, and id's

+ GET - /api/psychq/articles/?q={title/parent_course/id/universal_count}
        will retrieve posts associated with title/parent_course/id

+ GET - /api/psychq/articles/{id}
        will retrieve article associated with that id

+ POST - /api/psychq/articles/
            -id
            -custom_ordering
            -title
            -description
            -article_content
            -parent_course
            -source
            -est_time
            -thumbnail
            -full_res_image
            -universal_count
            -course_count
            -tags
            -reads
            -downloads
            -shares
            -timestamp {generated Auto}
        will post object if model is valid

+ PUT - /api/psychq/articles/{id {article_id}}
        will replace the object related to that id/pk

+ PATCH - /api/psychq/articles/{id}
        can update individual properties of an object
        as well as the whole object related t0 that id

