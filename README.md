Django-pages
============
A simple CMS extension for Django. It features a GRID to structure content on pages. The backend uses semantic-ui for
it's templates. You can use semantic-ui also to quickly create a nice frontend also. By configuring the GRID to only 
use 12 columns you can bootstrap your way to heaven when integrating the pages into your own design/template.

Pages are stored in the DB using an hierarchical structure so it's easy to create crumblepaths and nested menu's

GRID?
-----
A GRID can consist out of up to 16 columns. Cells can contain a variety of content:
- text (makes use of ckeditor inline editing)
- images
- FAQ
- imageslider
- address


Populate stuff
--------------
Run 
python manage.py populatepages


Todo
----
More tests, documentation via Sphinx and the release of v0.1
