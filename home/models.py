from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class HomePage(Page):
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('section', blocks.StructBlock([
                     ('title_section', blocks.CharBlock()),
                     ('content', blocks.RichTextBlock()),
                     ('img', ImageChooserBlock(required=False)),
                    ], template='streams/blocks/section.html',  icon='user')
         )
    ])

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        StreamFieldPanel('body', classname="full"),
    ]
