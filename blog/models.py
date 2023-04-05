from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class SiteUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"
        
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.caption}"

class Category(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="posts", null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="", related_name="categories")
    content = models.TextField(validators=[MinLengthValidator(14), MaxLengthValidator(6500)], default="Coming soon...")
    date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to="posts", default="default_post_img.jpg")
    current_tags = models.CharField(null=True,editable=False,max_length=15)
    slug = models.SlugField(blank=True, editable=False)


    def __str__(self):
        return f"{self.title}"

    def exrt(self):
        excerpt = self.content[:240]+"..."
        return excerpt

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def num_comments(self):
        number_of_comments = Post.objects.get(title=self.title).comments.all().count()
        return number_of_comments
    
    def all_tags(self):
        self.current_tags = Post.objects.get(title=self.title).tags.all()
        return self.current_tags

class Comment(models.Model):
    name = models.CharField(max_length=25)
    comment = models.TextField(max_length=600)
    date = models.DateField(auto_now_add=True)
    user_pic = models.ImageField(default="default_pfp.png")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")

    def __str__(self):
        return f"{self.name} -> {self.post.title}"

class Staff(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField(max_length=600)
    image = models.ImageField(upload_to="staffs", default="default_pfp.png")
    position = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)], null=True)

    def __str__(self):
        return f"{self.name}"

class About(models.Model):
    about = models.TextField(max_length=1500)

    def __str__(self):
        return f"About Us"