# mentor/models.py
from django.db import models
from django.contrib.auth.hashers import make_password

class Mentor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    linkedin_url = models.URLField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    mentor_image = models.ImageField(upload_to='mentors/', blank=True, null=True)
    mentor_company = models.CharField(max_length=255, blank=True, null=True)
    mentor_experience = models.PositiveIntegerField(help_text="Years of experience", default=0)
    skills = models.CharField(max_length=500, blank=True, null=True, help_text="Comma-separated skills")
    mentor_designation = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255,blank=False)
    confirm_password = models.CharField(max_length=255,blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Before saving, ensure the password is hashed
        if self.password:
            self.password = make_password(self.password)
        
        # Ensure that password and confirm_password match
        if self.password != self.confirm_password:
            raise ValueError("Password and Confirm Password do not match")
        
        super(Mentor, self).save(*args, **kwargs)