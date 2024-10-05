from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


STATUS = ((0, "Waiting"), (1, "Pulished"))


# Create post models.
class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_post"
    )
    subtitle = models.TextField(max_length=500, default=None)
    details = models.TextField(default=None)
    pub_time = models.CharField(max_length=10, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    bookmarks = models.ManyToManyField(
        User, default=None, related_name="news_bookmark", blank=True)
    likes = models.ManyToManyField(
        User, related_name="news_like", blank=True)

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):
        """Get url after user add and edit post"""
        return reverse('post_detail', kwargs={'slug': self.slug})
        
        # Add string that returns representation of an object.
    def __str__(self):
        return f"{self.title}"
    
     # Returns total number of bookmarks on a post.
    def number_of_bookmarks(self):
        return self.bookmarks.count()
        
        # Returns total number of likes on a post.
    def number_of_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    bio = models.TextField()
    my_pic = models.ImageField(
        null=True, blank=True, upload_to='profile_image'
    )

    def __str__(self):
        return self.user.username


# Add comment models.
class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
        