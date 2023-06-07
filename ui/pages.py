from iommi import Page, html, Menu, MenuItem, LAST
from django.template import Template
from camerahub import settings

menu = Menu(
    sub_menu=dict(
        root=MenuItem(url='/'),
        manufacturers=MenuItem(url='/ui/manufacturer'),
        form_examples=MenuItem(url='/form'),
        table_examples=MenuItem(url='/table'),
        menu_examples=MenuItem(url='/menu'),
        supernaut=MenuItem(url='/supernaut'),
        admin=MenuItem(url='/iommi-admin'),
        login=MenuItem(
            display_name='Log in',
            url='/iommi-admin/login/?next=/',
            include=lambda request, **_: not request.user.is_authenticated,
        ),
        log_out=MenuItem(
            display_name='Log out',
            url='/iommi-admin/logout/',
            include=lambda request, **_: request.user.is_authenticated,
        ),
    )
)

class BasePage(Page):
    menu = menu

    header = html.h1('CameraHub')
    logo = html.img(
        attrs__src='https://docs.iommi.rocks/en/latest/_static/logo_with_outline.svg',
        attrs__style__width='30%',
    )

    subtitle = html.h2('CameraHub')

    footer = html.div(
        html.hr(),
        #<p align="center">

        html.p(

            html.a(
                html.img(
                    attrs=dict(
                        src="/static/svg/facebook.svg",
                        width="30",
                        height="30",
                        alt="Facebook",
                        title="Facebook",
                    )
                ),
                attrs__href='https://www.facebook.com/camerahubapp',
                attrs__target='_blank',
            ),
            html.a(
                html.img(
                    attrs=dict(
                        src="/static/svg/github.svg",
                        width="30",
                        height="30",
                        alt="Github",
                        title="Github",
                    )
                ),
                attrs__href='https://github.com/camerahub/camerahub',
                attrs__target='_blank',
            ),
            html.a(
                html.img(
                    attrs=dict(
                        src="/static/svg/mail.svg",
                        width="30",
                        height="30",
                        alt="Mail",
                        title="Mail",
                    )
                ),
                attrs__href='mailto:support@camerahub.info',
                attrs__target='_blank',
            ),
            html.a(
                html.img(
                    attrs=dict(
                        src="/static/svg/icons8.svg",
                        width="30",
                        height="30",
                        alt="Icons8",
                        title="Icons8",
                    )
                ),
                attrs__href='https://icons8.com/icons',
                attrs__target='_blank',
            ),
            html.a(
                html.img(
                    attrs=dict(
                        src="/static/svg/status.svg",
                        width="30",
                        height="30",
                        alt="Status",
                        title="Status",
                    )
                ),
                attrs__href=settings.STATUS_URL,
                attrs__target='_blank',
            ),
            html.br(),
            html.small('CameraHub ',
                html.a('v0.0.0', attrs__href="https://github.com/camerahub/camerahub/releases/tag/0.0.0", attrs__target='_blank',),
            ),
        attrs=dict(
            align="center"
        )),        
        after=LAST
    )

class IndexPage(BasePage):

    subtitle = html.h4(
        html.img(
            attrs=dict(
                src="/static/svg/home.svg",
                width="30",
                height="30",
                alt="Home",
                title="Home",
            )
        ),
        'Welcome',
    )

    other_stuff = Template('index.html')

#{% if "test" in request.get_host or "localhost" in request.get_host %}
#<div class="alert alert-warning" role="alert">CameraHub is running in development or testing mode</div>
#{% endif %}

#<div class="jumbotron">
 #   html.div()


#    <div class="row">
#        <div class="col-sm-9">
#            <h1 class="display-4">Welcome to CameraHub</h1>
#            <p class="lead">an app for cataloguing vintage cameras, lenses, films, negatives &amp; prints</p>
#        </div>
#        <div class="col-sm-3">
#            <img src="{% static "svg/camera.svg" %}" class="float-right img-fluid" style="max-width:128px"
#                alt="CameraHub">
#        </div>
#    </div>
#    <hr class="my-4">
#    {% if user.is_authenticated %}
#    <p>Welcome back, {{ user.username }}.
#        {% else %}
#    <p>CameraHub is a public database of cameras, lenses and accessories, available to everyone. Registered users can
#        add or edit data. They can also keep a private collection of their cameras and lenses. Check out the
#        Concepts page for more info.</p>
#    <p><a class="btn btn-primary btn-sm" href="{% url 'login' %}" role="button">Login</a> or <a
#            class="btn btn-primary btn-sm" href="{% url 'django_registration_register' %}" role="button">Register</a> to
#        start tracking private data about your own collection.
#        {% endif %}#

#        Get started using the icons below, or use the menus above.</p>
#    <div class="card-deck">
#        <div class="card">
#            <a href="{% url 'schema:cameramodel-list' %}"><img class="card-img-top p-5" src="{% static "svg/camera.svg" %}"
#                    alt="Camera models"></a>
#            <div class="card-body">
#                <a href="{% url 'schema:cameramodel-list' %}">
#                    <h5 class="card-title">Camera models</h5>
#                </a>
#            </div>
#        </div>
#        <div class="card">
#            <a href="{% url 'schema:lensmodel-list' %}"><img class="card-img-top p-5"
#                    src="{% static "svg/teleconverter.svg" %}" alt="Lens models"></a>
#            <div class="card-body">
#                <a href="{% url 'schema:lensmodel-list' %}">
#                    <h5 class="card-title">Lens models</h5>
#                </a>
#            </div>
#        </div>
#        <div class="card">
#            <a href="{% url 'schema:filmstock-list' %}"><img class="card-img-top p-5" src="{% static "svg/film.svg" %}"
#                    alt="Film stocks"></a>
#            <div class="card-body">
#                <a href="{% url 'schema:filmstock-list' %}">
#                    <h5 class="card-title">Film stocks</h5>
#                </a>
#            </div>
#        </div>
#    </div>
#</div>
#{% endblock %}
