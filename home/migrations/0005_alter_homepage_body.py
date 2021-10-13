# Generated by Django 3.2.8 on 2021-10-13 15:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211013_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StructBlock([('title_section', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock()), ('img', wagtail.images.blocks.ImageChooserBlock(required=False))], icon='user'))]),
        ),
    ]