from django.db import models


class Aleatoire(models.Model):
    titre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.titre


class Formation(models.Model):
    titre = models.CharField(max_length=50, unique=True)
    sous_titre = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titre


class Commentaire(models.Model):
    nom = models.CharField(max_length=100, verbose_name='Nom')
    profession = models.CharField(max_length=50, verbose_name='Profession')
    message = models.TextField(max_length=500)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    publie = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nom


class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nom
