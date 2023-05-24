from iommi import Page, html, Menu, MenuItem, LAST
from camerahub import settings

menu = Menu(
    sub_menu=dict(
        root=MenuItem(url='/'),
        page_examples=MenuItem(url='/page'),
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

    header = html.h1('Welcome to iommi examples application')
    logo = html.img(
        attrs__src='https://docs.iommi.rocks/en/latest/_static/logo_with_outline.svg',
        attrs__style__width='30%',
    )

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
    title = html.h1('CameraHub')
    welcome_text = 'This is a database of cameras'
