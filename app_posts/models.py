from django.db import models
from django.utils.text import slugify


from app_accounts.models import CustomUser
from app_categories.models import Category





class Post(models.Model):
    
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name="Slug (URL)")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to="posts/", null=True, blank=True, verbose_name="Post rasmi")
    author = models.ForeignKey( to=CustomUser, verbose_name="Muallif", on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, verbose_name="Categoriya", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True , verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True , verbose_name="Yangilangan vaqti")
    
   
   
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"
        ordering = ['-created_at']  
        
        
    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)