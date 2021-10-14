from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
)


class FormField(AbstractFormField):
    page = ParentalKey(
        'AppointmentPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class AppointmentPage(AbstractEmailForm):

    intro = RichTextField(blank=True)
    tank_you = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('intro'),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("tank_you"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address", classname="col-6"),
                FieldPanel("to_address", classname="col-6"),
            ]),
            FieldPanel("subject")
        ], heading="Email Settings")
    ]
    template = "form/index_form.html"
