from django.db import models

# Create your models here.


class OBECB(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class Sex(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class InsuranceCompany(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    ico = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=200, default="")
    data_box = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.name}"


class KSTPR(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class STPR(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False, )
    code_2 = models.CharField(max_length=2, blank=True, null=True, default="")
    code_3 = models.CharField(max_length=3, blank=True, null=True, default="")

    def __str__(self):
        return f"{self.name}"


class OKRESB(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class ODHL(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class STUPEN(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class KOD_ZAH(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class KOD_UKON(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class ROCNIK(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class PRIZN_ST(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class ZPUSOB(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class DRST(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class DELST(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class OBOR(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False, default="7941K41")

    def __str__(self):
        return f"{self.name}"


class OBOR2(models.Model):
    id = models.CharField(max_length=20, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False, default="7941K41")

    def __str__(self):
        return f"{self.name}"


class FST(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class ForeignLanguage(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class FieldLanguage(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class FIN(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class KOD_ZMEN(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class KOD_VETY(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class ST_SKOLY(models.Model):
    id = models.CharField(max_length=8, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class P_JAZ(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class KOD_ZK(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class ExamType(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


class Success(models.Model):
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f"{self.name}"


# class LET_PSD(models.Model):
#     id = models.CharField(max_length=5, primary_key=True, unique=True)
#     name = models.CharField(max_length=200, blank=True)
#
#     def __str__(self):
#         return f"{self.name}"


class PRERUS(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"
