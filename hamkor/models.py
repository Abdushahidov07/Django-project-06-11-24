from django.db import models

# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    age =  models.IntegerField()
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=None) 
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.username
    


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.category_name
    

class Skills(models.Model):
    skill_name = models.CharField(max_length=50)
    description = models.TextField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.skill_name
    

class City(models.Model):
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name


class Region(models.Model):
    region_name = models.CharField(max_length=50)
    def __str__(self):
        return self.region_name
    
    

class Street(models.Model):
    street_name = models.CharField(max_length=50)
    def __str__(self):
        return self.street_name
    
    

class Problems(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,  on_delete=models.CASCADE)
    city_id =  models.ForeignKey(City,  on_delete=models.CASCADE)
    region_id =  models.ForeignKey(Region,  on_delete=models.CASCADE)
    street_id =  models.ForeignKey(Street,  on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/images', height_field=None, width_field=None, max_length=None)
    status = models.BooleanField(default=False)
    is_activ = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
    


class Application(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    problems_id = models.ForeignKey(Problems, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    is_activ = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.message
    
