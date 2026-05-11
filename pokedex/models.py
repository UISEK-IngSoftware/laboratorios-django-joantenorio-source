from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    birthdate = models.DateField(null=False)
    level = models.IntegerField(null=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pokemon(models.Model):
    POKEMON_TYPES = {
        ('A', 'Agua'),
        ('F', 'Fuego'),
        ('T', 'Tierra'),
        ('P', 'Planta'),
        ('E', 'Eléctrico'),
        ('L', 'Lagartija'),
    }
    
    name = models.CharField(max_length=30, null=False)
    type = models.CharField(max_length=30, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(decimal_places=4, max_digits=6)
    height = models.DecimalField(decimal_places=4, max_digits=6)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.ImageField(upload_to='pokemon_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name