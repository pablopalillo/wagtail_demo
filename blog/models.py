from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogPage(Page):
    custom_title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="Title of blog page"
    )

    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration")
    ]

    template = "blog/index_blog.html"

    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context['blog_entries'] = BlogDetailPage.objects.live().public()
        return context

    class Meta:
        verbose_name = "Blog Index Page"


class BlogDetailPage(Page):
    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]

    template = "blog/blog_post.html"

    class Meta:
        verbose_name = "Blog Post"
