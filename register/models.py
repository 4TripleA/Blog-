from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
#for uploading files to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class blogpost(models.Model):
    title = models.CharField(max_length=150) 
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 
    def __str__(self):
      return self.title    
 
class profilepage(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='image')
    bio = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.bio
    
