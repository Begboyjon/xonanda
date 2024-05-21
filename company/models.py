from django.db import models

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=25)
    subject = models.CharField(max_length=50)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        return self.image.url

    def __str__(self):
        return f"{self.id}--{self.teacher_name}"


class Abouts(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/path/to/default/image"  # Optional: Default image URL

    def __str__(self):
        return f"{self.id}"  # Adjust as needed, e.g., `self.teacher_name` if uncommented

class Contacts(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/path/to/default/image"  # Optional: Default image URL

    def __str__(self):
        return f"{self.id}" # Adjust as needed, e.g., `self.teacher_name` if uncommented




