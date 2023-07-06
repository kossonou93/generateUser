from django.db import models
import psycopg2 as Database

class User(models.Model):

    GENRE_MALE = 'male'
    GENRE_FEMELE = 'femele'
    GENRE_CHOICES = (
        (GENRE_MALE, 'Male'),
        (GENRE_FEMELE, 'Femele')
    )

    gender = models.CharField(max_length=20, choices=GENRE_CHOICES)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    title_name = models.CharField(max_length=255, blank=True)
    number_location = models.IntegerField(blank=True)
    name_location = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    offset = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=255, blank=True)
    email = models.CharField(max_length=100, blank=True)
    uuid = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    salt = models.CharField(max_length=255, blank=True)
    md5 = models.CharField(max_length=255, blank=True)
    sha1 = models.CharField(max_length=255, blank=True)
    sha256 = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(blank=True)
    age = models.IntegerField(blank=True)
    phone = models.CharField(max_length=255, blank=True)
    cell = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{id} {gender} {first_name} {last_name} {title_name} {number_location} {name_location} {city} {state} {country} {postcode} {latitude} {longitude} {offset} {description} {email} {uuid} {username} {password} {salt} {md5} {sha256} {date} {age} {phone} {cell}'.format(
            id=self.pk,
            gender=self.gender,
            first_name=self.first_name,
            last_name=self.last_name,
            title_name=self.title_name,
            number_location=self.number_location,
            name_location=self.name_location,
            city=self.city,
            state=self.state,
            country=self.country,
            postcode=self.postcode,
            latitude=self.latitude,
            longitude=self.longitude,
            offset=self.offset,
            description=self.description,
            email=self.email,
            uuid=self.uuid,
            username=self.username,
            password=self.password,
            salt=self.salt,
            md5=self.md5,
            sha1=self.sha1,
            sha256=self.sha256,
            date=self.date,
            age=self.age,
            phone=self.phone,
            cell=self.cell,
        )



