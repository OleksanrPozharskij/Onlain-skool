import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
        id = models.AutoField(primary_key=True)
        owner = models.ForeignKey(User,
                                     related_name='courses_created',
                                     on_delete=models.CASCADE)
        subject = models.ForeignKey(Subject,
                                            related_name='courses',
                                            on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        slug = models.SlugField(max_length=200, null=False, blank=False)
        overview = models.TextField()
        created = models.DateTimeField(auto_now_add=True)
        students = models.ManyToManyField(User,
                                          related_name='courses_joined',
                                          blank=True)

        class Meta:
                ordering = ['-created']

        def __str__(self):
            return self.title

class Module(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,
                                related_name='modules',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    module = models.ForeignKey(Module,
                                related_name='contents',
                                on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                      on_delete=models.CASCADE,
                                      limit_choices_to={'model__in':(
                                                         'RichTextField',
                                                         'video',
                                                         'image',
                                                         'file')})

    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                                     related_name='%(class)s_related',
                                     on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
            self._meta.model_name), {'item': self})

class Text(ItemBase):
    id = models.AutoField(primary_key=True)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()

class File(ItemBase):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    id = models.AutoField(primary_key=True)
    url = models.URLField()

