from django.db import models
from django.contrib.auth.admin import User
from django.utils.text import slugify
from django.utils import timezone

class Post(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE, default= 1)
    title= models.CharField(max_length= 120)
    content= models.TextField()
    draft= models.BooleanField(default= False)
    created= models.DateTimeField(editable= False)
    modified= models.DateTimeField()
    slug= models.SlugField(unique= True, max_length=120, editable= False)
    image= models.ImageField(upload_to= 'post', null= True, blank= True)
    modifiedBy=models.ForeignKey(User, on_delete= models.SET_NULL, null= True, related_name= 'modified_by')

    def get_slug(self):
        slug= slugify(self.title.replace('ı', 'i'))
        unique= slug
        number= 1
        while Post.objects.filter(slug=unique):
            unique= '{}-{}'.format(slug, number)
            number+= 1
        return unique
    
    def __str__(self): # http://localhost:8000/admin/post/post/ sayfasinda baslik alaninda title gorunmesi icin
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created= timezone.now()
        self.modified= timezone.now()
        self.slug= self.get_slug()
        return super(Post, self).save(*args, **kwargs)