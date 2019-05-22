from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from finalyear.models import Center

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    center = models.ForeignKey(Center, on_delete=models.CASCADE,blank=True, null=True)
    id_number = models.IntegerField(blank=True, null=True)
    phonenumber = models.IntegerField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
