from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User2(AbstractUser):
    image = models.ImageField(null=True, blank=True)
    parol = models.CharField(max_length=50, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.username


class Dastur(models.Model):
    dasturnomi = models.TextField(max_length=500, null=True, blank=True)
    servernomi = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    pudratchi = models.TextField(max_length=500, null=True, blank=True)
    ishgatushgandavt = models.TextField(max_length=500, null=True, blank=True)
    tolovharajatlari = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, blank=True)
    tell = models.TextField(max_length=500, blank=True)
    login = models.TextField(max_length=500, null=True, blank=True)
    parol = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField( upload_to='shartnoma',null=True,blank=True)

    def __str__(self):
        return self.dasturnomi


class Internet(models.Model):
    cabinetlogin = models.TextField(max_length=500, null=True, blank=True)
    cabinetparol = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    pudratchi = models.TextField(max_length=500, null=True, blank=True)
    ishgatushgandavt = models.TextField(max_length=500, null=True, blank=True)
    tolovharajatlari = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.cabinetlogin


class Wifi(models.Model):
    adminlogin = models.TextField(max_length=500, null=True, blank=True)
    adminparol = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    qurulmarusumi = models.TextField(max_length=500, null=True, blank=True)
    xolati = models.TextField(max_length=500, null=True, blank=True)
    foydalanishgatopshirilganvaqti = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    wifinomi = models.TextField(max_length=500, null=True, blank=True)
    parol = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.adminlogin


class Kompyuter(models.Model):
    raqam = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    monitor = models.TextField(max_length=500, null=True, blank=True)
    protsesor = models.TextField(max_length=500, null=True, blank=True)
    matplata = models.TextField(max_length=500, null=True, blank=True)
    opiratevka = models.TextField(max_length=500, null=True, blank=True)
    videokarta = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    xolat = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.raqam


class Server(models.Model):
    raqam = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    monitor = models.TextField(max_length=500, null=True, blank=True)
    protsesor = models.TextField(max_length=500, null=True, blank=True)
    matplata = models.TextField(max_length=500, null=True, blank=True)
    opiratevka = models.TextField(max_length=500, null=True, blank=True)
    videokarta = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    xolat = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.raqam


class Hodim(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    lavozim = models.TextField(max_length=500, null=True, blank=True)
    vazifasi = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    pasportraqam = models.TextField(max_length=500, null=True, blank=True)
    jshir = models.TextField(max_length=500, null=True, blank=True)
    manzil = models.TextField(max_length=500, null=True, blank=True)
    oilaviyholat = models.TextField(max_length=500, null=True, blank=True)
    malumoti = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.name


class Kamera(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    holati = models.TextField(max_length=500, null=True, blank=True)
    rusumi = models.TextField(max_length=500, null=True, blank=True)
    xolat = models.TextField(max_length=500, null=True, blank=True)
    foydalanishgatopshirilganvaqt = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, null=True, blank=True)
    tel = models.TextField(max_length=500, null=True, blank=True)
    pudratchi = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.name


class Gps(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    tashkilotnomi = models.TextField(max_length=500, null=True, blank=True)
    holati = models.TextField(max_length=500, null=True, blank=True)
    rusumi = models.TextField(max_length=500, null=True, blank=True)
    xolat = models.TextField(max_length=500, null=True, blank=True)
    foydalanishgatopshirilganvaqt = models.TextField(max_length=500, null=True, blank=True)
    masul = models.TextField(max_length=500, null=True, blank=True)
    tel = models.TextField(max_length=500, null=True, blank=True)
    pudratchi = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)
    shartnoma = models.FileField(upload_to='shartnoma', null=True, blank=True)

    def __str__(self):
        return self.name


class Taklif(models.Model):
    name = models.TextField(max_length=500, null=True, blank=True)
    taklifsohasi = models.TextField(max_length=500, null=True, blank=True)
    tuliqtavsifi = models.TextField(max_length=500, null=True, blank=True)
    tell = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
