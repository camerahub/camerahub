from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# The text to put at the top of each admin page, as an <h1> (a string). By default, this is “Django administration”.
admin.site.site_header = 'PhotoDB'

# The text to put at the end of each admin page’s <title> (a string). By default, this is “Django site admin”.
admin.site.site_title = 'PhotoDB'

# The text to put at the top of the admin index page (a string). By default, this is “Site administration”.
admin.site.index_title = 'PhotoDB'

# The URL for the “View site” link at the top of each admin page. By default, site_url is /. Set it to None to remove the link.
admin.site.site_url = None