import os
from django.db import models
# Create your models here.
class AboutUs(models.Model): #goal
    title=models.CharField(max_length=256)
    discription=models.TextField()
    image=models.ImageField()

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        try:
            this = AboutUs.objects.get(id=self.id)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class LatestEvents(models.Model):
    image=models.ImageField()
    caption=models.CharField(max_length=250)
    def __str__(self):
        return self.caption
    def save(self, *args, **kwargs):
        try:
            this = LatestEvents.objects.get(id=self.id)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class HomepageOurTeam(models.Model):
    name=models.CharField(max_length=256)
    cader=models.CharField(max_length=256)
    image=models.ImageField()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        try:
            this = HomepageOurTeam.objects.get(id=self.id)
            print(this)
            print(self.image.name)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class AboutUsOurTeam(models.Model):
    name=models.CharField(max_length=256)
    cader=models.CharField(max_length=256)
    image=models.ImageField()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        try:
            this = AboutUsOurTeam.objects.get(id=self.id)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class WhyChooseUs(models.Model):
    theory=models.TextField()
    my_vision=models.TextField()
    my_mission=models.TextField()
    my_history=models.TextField()
    def __str__(self):
        return self.my_vision
class Gallary(models.Model):
    aboutus=models.ForeignKey(AboutUs,on_delete=models.CASCADE)
    image=models.ImageField()
    def __str__(self):
        return self.image.name
    def save(self, *args, **kwargs):
        try:
            this = Gallary.objects.get(id=self.id)
            print(this)
            print(self.image.name)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class ContactUs(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    message=models.TextField()
    def __str__(self):
        return self.name
class CountNumbers(models.Model):
    food_feeded=models.IntegerField()
    sanitary_pads=models.IntegerField()
    education=models.IntegerField()
    rice_groceries=models.IntegerField()
    funerals=models.IntegerField()
    transformation=models.IntegerField()
    blankets       =models.IntegerField(default=0)
    organs       =models.IntegerField(default=0)
    blood_camps       =models.IntegerField(default=0)
class Achivements(models.Model):
    image=models.ImageField()
    title=models.CharField(max_length=100,default="Our Achievement")
    def __str__(self):
        return self.image.name
    def save(self, *args, **kwargs):
        try:
            this = Achivements.objects.get(id=self.id)
            print(this)
            print(self.image.name)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class NGOPartners(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.image.name
    def save(self, *args, **kwargs):
        try:
            this = NGOPartners.objects.get(id=self.id)
            print(self.image.name)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class SocialMediaPartners(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField()
    def __str__(self):
        return self.image.name
    def save(self, *args, **kwargs):
        try:
            this = SocialMediaPartners.objects.get(id=self.id)
            print(self.image.name)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)
class BannerImage(models.Model):
    image=models.ImageField()
    def __str__(self):
        return self.image.name
    def save(self, *args, **kwargs):
        try:
            this = BannerImage.objects.get(id=self.id)
            print(self.image.name)
            if this.image != self.image:
                os.remove(this.image.path)
        except:
            pass
        super().save(*args, **kwargs)
    def delete(self,*args,**kwargs):
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args,**kwargs)


class TestMonial(models.Model):
    comment = models.CharField(max_length=260)
    name    = models.CharField(max_length=260)

    def __str__(self):
        return self.name
