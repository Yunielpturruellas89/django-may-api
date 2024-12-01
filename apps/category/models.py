from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    views = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug: # Only generate slug if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)  # Call the original save method

    def get_view_count(self):
         views = ViewCount.objects.filter(category = self).count()
         return views
    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class ViewCount(models.Model):
        category = models.ForeignKey(Category, related_name='category_view_count', on_delete=models.CASCADE)
        ip_address = models.CharField(max_length=255)

        def __str__(self):
             return f"{self.ip_address}"