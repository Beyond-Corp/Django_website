from django.utils import timezone

from django.db import models


class ArticleSeries(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    slug = models.CharField("Series Slug", null=False, blank=False, unique=True, max_length=200)
    published = models.DateTimeField("Date published", default=timezone.now)

    def __str__(self):
        return self.title # car on veut que le dashboard, on puisse avoir le nom des documents directement . pour verifier commante et observe le dashborad

    class Meta:
        verbose_name_plural = "Series"


class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    article_slug = models.CharField("Article Slug", null=False, blank=False, unique=True, max_length=200)
    content = models.CharField()
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    Series = models.ForeignKey(ArticleSeries, default="",verbose_name="Series",on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title  # car ....

    @property
    def slug(self):
        return self.article_slug
