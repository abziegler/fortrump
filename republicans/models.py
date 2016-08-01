from django.db import models

# Create your models here.

class Republican(models.Model):
    last_name = models.CharField(max_length=31)
    first_name = models.CharField(max_length=31)
    state = models.CharField(max_length=2)
    twitter_id = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31, unique=True)

    SENATOR = 'S'
    REPRESENTATIVE = 'R'
    GOVERNOR = 'G'
    TYPE_CHOICES = (
        (SENATOR, 'Senator'),
        (REPRESENTATIVE, 'Representative'),
        (GOVERNOR, 'Governor'),
    )
    gov_type = models.CharField(
        max_length=1,
        choices=TYPE_CHOICES,
        default=REPRESENTATIVE,
    )

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


