from django.db import models


class Chercheur(models.Model):
    chno = models.AutoField(primary_key=True)
    chnom = models.CharField(max_length=100)
    grade = models.CharField(max_length=2, blank=True, null=True)
    statut = models.CharField(max_length=1, blank=True, null=True)
    daterecrut = models.DateField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    prime = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    supno = models.ForeignKey('self', models.DO_NOTHING, db_column='supno', blank=True, null=True)
    labno = models.ForeignKey('Laboratoire', models.DO_NOTHING, db_column='labno', blank=True, null=True)
    facno = models.ForeignKey('Faculte', models.DO_NOTHING, db_column='facno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chercheur'


class Faculte(models.Model):
    facno = models.AutoField(primary_key=True)
    facnom = models.CharField(max_length=10)
    adresse = models.CharField(max_length=255)
    libelle = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'faculte'


class HistoriqueChercheurs(models.Model):
    chno = models.IntegerField(blank=True, null=True)
    chnom = models.CharField(max_length=100, blank=True, null=True)
    grade = models.CharField(max_length=2, blank=True, null=True)
    statut = models.CharField(max_length=1, blank=True, null=True)
    daterecrut = models.DateField(blank=True, null=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    action = models.CharField(max_length=20, blank=True, null=True)
    date_modification = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historique_chercheurs'


class Laboratoire(models.Model):
    labno = models.AutoField(primary_key=True)
    labnom = models.CharField(max_length=100)
    facno = models.ForeignKey(Faculte, models.DO_NOTHING, db_column='facno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laboratoire'


class Publication(models.Model):
    pubno = models.CharField(primary_key=True, max_length=7)
    titre = models.CharField(max_length=255)
    theme = models.CharField(max_length=50)
    type = models.CharField(max_length=2, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    apparition = models.CharField(max_length=255, blank=True, null=True)
    editeur = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publication'


class Publier(models.Model):
    chno = models.OneToOneField(Chercheur, models.DO_NOTHING, db_column='chno', primary_key=True)  # The composite primary key (chno, pubno) found, that is not supported. The first column is selected.
    pubno = models.ForeignKey(Publication, models.DO_NOTHING, db_column='pubno')
    rang = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publier'
        unique_together = (('chno', 'pubno'),)
