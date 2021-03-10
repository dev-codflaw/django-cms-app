from django.db import models




class CarouselSlide(models.Model):
    slide_name = models.CharField(max_length=150)
    slide_img = models.ImageField(upload_to="uploads/slider")
    slide_slug = models.SlugField()
    title_on_slide = models.CharField(max_length=250, blank=True, null=True)
    desc_on_slide = models.TextField(max_length=500, blank=True, null=True)
    call_to_action_link_on_slide = models.CharField(max_length=250, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slide_name

    class Meta:
        db_table = 'carousel_slides'




class Carousel(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField(max_length=500)
    images = models.ManyToManyField(CarouselSlide)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'carousel'