from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models



class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        max_length=15,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex='^[a-zA-Z0-9_]*$',
                message="Ensure this value contains only letters, numbers, and underscore.",
            )
        ],
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    album_name = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        unique=True,
    )
    artist = models.CharField(
        blank=False,
        null=False,
        max_length=30,
    )

    genre = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        choices=(
            ('Pop Music', 'Pop Music'),
            ('Jazz Music', 'Jazz Music'),
            ("R&B Music", "R&B Music"),
            ("Rock Music", "Rock Music"),
            ("Country Music", "Country Music"),
            ("Dance Music", "Dance Music"),
            ("Hip-Hop Music", "Hip-Hop Music"),
            ("Other", "Other"),
        )
    )
    description = models.TextField(
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,

    )
    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0)]
    )
    profile = models.ForeignKey(
        to=Profile, on_delete=models.CASCADE
    )