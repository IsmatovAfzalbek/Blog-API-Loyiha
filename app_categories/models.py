from django.db import models
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=120, unique=True, blank=True, verbose_name="Slug (URL)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['-created_at']  
        
        
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    