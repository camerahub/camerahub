About
#####

CameraHub is an app for cataloguing vintage cameras, lenses, films, negatives & prints. This page has extra background information about CameraHub.

History
-------

CameraHub started out as a pet project of photographer and camera collector `Jonathan Gazeley <https://jonathangazeley.com/>`_.
He started using a MySQL database to track his cameras and lenses, and later his films, negatives and prints. As the database grew,
it became more difficult to manage, so he wrote a set of helper scripts in Perl.

Jonathan thought that this collection of Perl scripts and a database might be helpful to others, so the
`PhotoDB <https://github.com/djjudas21/photodb-perl>`_ project was born. PhotoDB was a command-line app written in Perl which
was able to to catalog cameras, lenses, accessories, films, negatives, prints and scans. It was also able to write EXIF tags
(such as date/time stamps, geotags and data about the camera) to JPGs scanned from negatives, so they could be catalogued with any
digital photo library. PhotoDB had a number of releases and was nearing feature-completion as an app. Despite the database backend
being comprehensive, it had a fairly impenetrable command-line user interface that never achieved traction with the photography
community. The source code for PhotoDB is still available, but development has ceased.

CameraHub is the latest generation of the project. It uses the same database schema as PhotoDB but has a completely new user
inteface, written in Python and Django as a web application, that allows it to be accessed on virtually any device and makes it
easier for all photographers and collectors to track their collection.

Other sites
-----------

There are many websites with information about camera equipment but most of these sites have primarily text-based
information - for example, the excellent `Camera Wiki <http://camera-wiki.org/wiki/Main_Page>`_ resource.
By contrast, CameraHub centres around
numerical, normalised, structured data that allows easy searching and sorting and the modelling of relationships
between equipment and images. Relational data allows CameraHub to do things like show you all lenses that work with
a particular camera, or all pictures you took with a particular lens.

Another popular site is `CollectiBlend <https://collectiblend.com/>`_, which offers a more data-oriented experience.
However, it prioritises pricing information and doesn't include much data about the cameras and lenses themselves.

CameraHub also offers unique features for cataloguing films, negatives, prints and scans.

Community
---------

With a project like CameraHub, building a community is key. CameraHub provides a platform, but it is useless without
good quality data. This is where the community comes in - collectively gathering and entering data so everyone can benefit.

For example, you might buy a camera on eBay, wish to catalogue it, and find that it is not yet in CameraHub. You'd do some
research online, enter it into CameraHub and add it to your collection. The next person who wants to catalogue the same camera
wouldn't need to enter the data again - the camera you entered is available to everyone, and anyone can add it to their collection too.

As well as the community around CameraHub itself, there is a `CameraHub Facebook page <https://www.facebook.com/camerahubapp/>`_
where you can keep up to date with news.

Support
-------

If you get stuck with CameraHub, informal support is available by messaging `CameraHub on Facebook <https://www.facebook.com/camerahubapp/>`_,
or by sending an email to support@camerahub.info. If you think you've found a bug in CameraHub,
or if you want to suggest a new feature, you can `log an issue on Github <https://github.com/camerahub/camerahub/issues>`_.

Roadmap
-------

CameraHub is an evolving project. For a detailed look at current bugs and feature requests, check out the
`issue tracker <https://github.com/camerahub/camerahub/issues>`_. Anyone can report bugs, request features and contribute code.
