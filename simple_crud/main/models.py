from django.db import models

class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField(blank=True, null=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dostepny = models.BooleanField(default=True)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazwa