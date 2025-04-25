from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class subjects(models.Model):
    type = models.CharField(max_length=100)


    def __str__(self):
        return self.type

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(subjects, related_name="subjects")
    rate_min = models.BigIntegerField(
        null=True, blank=True, 
        validators=[MinValueValidator(0), MaxValueValidator(9999)]  # Min value 0, Max value 5000
    )
    rate_max = models.IntegerField(
        null=True, blank=True, 
        validators=[MinValueValidator(0), MaxValueValidator(10000)]  # Min value 0, Max value 10000
    )
    image = models.ImageField(upload_to='images/', blank=True)  # images/ is the subfolder in MEDIA_ROOT

    def validate_rate(self):
    # Custom validation: rate_max should always be greater than rate_min
        if self.rate_min is not None and self.rate_max is not None:
            if self.rate_max < self.rate_min:
                raise ValidationError({'rate_max': 'rate_max cannot be less than rate_min.'})

    def __str__(self):
        return self.name