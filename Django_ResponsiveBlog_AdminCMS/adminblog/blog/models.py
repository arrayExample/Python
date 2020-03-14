from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class homepageMessage(models.Model):
    title = models.CharField(max_length=150)
    message = RichTextField()

    class Meta:
        verbose_name_plural = "Homepage Message"

    def save(self, *args, **kwargs):
        super(homepageMessage, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/'+slugify(self.title)
