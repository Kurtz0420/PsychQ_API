PsychQ Api
===========

For PsychQ App Backend

+ Will have one superUser that can GET, PUT, PATCH, DELETE data

+ Will have just one app POSTS that will contain all the models

+

 '/admin' - admin panels func : all control
 'api/posts/ - will list the items in the database as well as ability to post new item
 'api/posts/{number} - will return the object of the respective id
 'api/posts/?q={fieldsProvidedIn 'PostApiView.get_query} - searches the title/data inside items
