from django.db import models

# Create your models here.
class Mot(models.Model):
    orthographe = models.CharField(max_length=32, error_messages="Un mot ne doit pas dépasser 128 caractères !")
    signification = models.TextField(error_messages="L'explication du terme est obligatoire !")
    traduction_ang = models.CharField(max_length=48, error_messages="L'équivalent en anglais doit avoir au plus 48 caractères !")
    traduction_mat = models.CharField(max_length=48, error_messages="L'équivalent en anglais doit avoir au plus 48 caractères !")
    context = models.CharField(max_length=32, error_messages="Veuillez renseigner le contexte d'utilisation du mot")
    exemple = models.TextField(blank=True, null=True) # blank=True, null=True vont toujours de paire

    # Dans le panneau d'admin des blog, ce sont les titres des blog qui seront affichés.
    def __str__(self):
        return self.orthographe