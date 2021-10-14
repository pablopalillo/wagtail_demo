from django.db import models
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class CTABlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.CharBlock(max_length=100)
    button_page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock(required=True)

    class Meta:
        template = "streams/blocks/cta_block.html"
        icon = "placeholder"
        label = "Call To Action"


class HomePage(Page):
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('section', blocks.StructBlock([
                     ('title_section', blocks.CharBlock()),
                     ('content', blocks.RichTextBlock()),
                     ('img', ImageChooserBlock(required=False)),
                    ], template='streams/blocks/section.html',  icon='user')

         ),
        ('cta', CTABlock())
    ])

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        StreamFieldPanel('body', classname="full"),
    ]
