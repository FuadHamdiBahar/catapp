from django.db import models

# Create your models here.


class Soal(models.Model):
    foto_soal = models.ImageField(upload_to='img')

    def __str__(self):
        return "{}".format(self.id)


class KombinasiSoal(models.Model):
    # no_kombinasi = models.IntegerField()
    foto_kombinasi = models.ImageField(upload_to='img/kombinasi')

    def __str__(self):
        return "Nomor {}".format(self.id)
