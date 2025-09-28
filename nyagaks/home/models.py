from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from django import forms
from wagtail.search import index
from wagtail.core.models import Page


class HomePage(Page):
    pass


class AboutPage(Page):
    team_title = models.TextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('team_title'),
        InlinePanel('portfolio_images', label="Team Members"),

    ]
    InlinePanel('portfolio_images', label="Project images")


class portfolio_images(Orderable):
    Page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name="portfolio_images")
    lawyer_title = models.TextField(blank=True)
    lawyer_description = models.TextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, null=True, related_name='+'
    )
    panels = [
        FieldPanel('lawyer_title'),
        FieldPanel('lawyer_description'),
        ImageChooserPanel('image'),
    ]


class ServicesPage(Page):
    pass
