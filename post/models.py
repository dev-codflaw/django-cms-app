from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField


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
    slug = models.SlugField(unique=True, blank=True, max_length=250, help_text="Make your own slug or it will be copy from title.")
    image = models.ImageField(upload_to="category/images", blank=True, null=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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
    title = models.CharField(max_length=500)
    keyword = models.CharField(max_length=250, blank=True, help_text="SEO keyword")
    description = models.TextField(max_length=500, blank=True, help_text="SEO description")
    image = models.ImageField(upload_to="posts/images", blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, max_length=250, help_text="Make your own slug or it will be copy from title.")
    content = RichTextField(blank=True, null=True) # for ckeditor 
    # content = HTMLField(blank=True, null=True) # for tinymce
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'posts'
        



