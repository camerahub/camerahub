from iommi import Page, Fragment, html, LAST
from camerahub import settings


class BasePage(Page):
    menu = Fragment(template='nav.html')

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

    other_stuff = Fragment(template='index.html')
