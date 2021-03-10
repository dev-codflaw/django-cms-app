from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Tag(models.Model):
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=100, default='#cfcfcf')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table='tags'

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()
    image = models.ImageField(upload_to="uploads/cat_images", blank=True, null=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    
    class Meta:
        unique_together = ('slug', 'parent')
        db_table = 'category'


class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to="uploads/posts", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, max_length=250)
    description = RichTextField(blank=True, null=True)
    status = models.BooleanField(default=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'posts'
        



