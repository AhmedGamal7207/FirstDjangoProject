from django.db import models

# Create your models here.
class Post(models.Model):
    # Here we add our fields
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    text = models.TextField()

    # To have titles appear in the table in admin page
    def __str__(self):
        return self.title
    
