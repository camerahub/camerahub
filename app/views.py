from schema import models
from iommi import Table, Page, Style, html, Column, Action

class BasePage(Page):
    pass

class cameramodel_list(BasePage):
    #h4 = html.h4('Camera Models')

    h5 = html.h5(
        #html.img('camerahub.svg'),
        html.img(attrs=dict(src='/static/svg/camera.svg', alt='pic', width='30', height='30')),
        Action.icon('edit', attrs__href="edit/"),
        Action(
            display_name='',
            attrs__href='link.com',
            #template=Template("<img src='/static/svg/camera.svg', alt='pic', width='30', height='30'>")
        ),
        #html.a(attrs=dict(href=models.CameraModel.get_absolute_url)),
        Action(display_name='Do this', attrs__href='link.com'),
        html.h4(models.CameraModel._meta.verbose_name_plural),
    )
    desc = html.p(models.CameraModel.description())

#<h4><img src="{% get_static_prefix %}svg/{{ view.model.icon }}" alt="{{ view.model | verbose_name | title}}"
#        width="30" height="30">
#    <a href="{% url view.model|model_list %}">{{ view.model | verbose_name_plural | title }}</a></h4>

    cameramodels = Table(
        auto__model=models.CameraModel,

        auto__include=['manufacturer', 'model', 'mount', 'format', 'introduced', 'negative_size'],

        columns__manufacturer__filter__include=True,
        columns__model__filter__include=True,
        columns__format__filter__include=True,
        columns__negative_size__filter__include=True,
        columns__body_type__filter__include=True,
        
    )
