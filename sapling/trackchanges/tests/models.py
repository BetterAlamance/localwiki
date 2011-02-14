from django.db import models

from trackchanges.models import TrackChanges

"""
TODO: It would be cool to write a little thing to randomly generate
model definitions for tests.
"""

class M1(models.Model):
    a = models.CharField(max_length=200)
    b = models.CharField(max_length=200)
    c = models.CharField(max_length=200)
    d = models.CharField(max_length=200)

    history = TrackChanges()

class M2(models.Model):
    a = models.CharField(max_length=200)
    b = models.TextField()
    c = models.IntegerField()

    history = TrackChanges()

class M3BigInteger(models.Model):
    a = models.CharField(max_length=200)
    b = models.BooleanField(default=False)
    c = models.BigIntegerField()

    history = TrackChanges()

class M4Date(models.Model):
    a = models.DateTimeField(auto_now_add=True)
    b = models.DateField(auto_now_add=True)

    history = TrackChanges()

class M5Decimal(models.Model):
    a = models.DecimalField(max_digits=19, decimal_places=3)
    b = models.DecimalField(max_digits=5, decimal_places=2)

    history = TrackChanges()

class M6Email(models.Model):
    a = models.EmailField()

    history = TrackChanges()

class M7Numbers(models.Model):
    a = models.FloatField()
    b = models.PositiveIntegerField()
    c = models.PositiveSmallIntegerField()
    d = models.SmallIntegerField()

    history = TrackChanges()

class M8Time(models.Model):
    a = models.TimeField(auto_now_add=True)

    history = TrackChanges()

class M9URL(models.Model):
    a = models.URLField(verify_exists=False)

    history = TrackChanges()

class M10File(models.Model):
    a = models.FileField(upload_to='test_trackchanges_uploads')

    history = TrackChanges()

class M11Image(models.Model):
    a = models.ImageField(upload_to='test_trackchanges_uploads')

    history = TrackChanges()

class M12ForeignKey(models.Model):
    a = models.ForeignKey(M2)
    b = models.CharField(max_length=200)

    history = TrackChanges()

class M12ForeignKeysRelatedSpecified(models.Model):
    a = models.ForeignKey(M2, related_name="g")
    b = models.CharField(max_length=200)

    history = TrackChanges()

class M13ForeignKeySelf(models.Model):
    a = models.ForeignKey('self', null=True)
    b = models.CharField(max_length=200)

    history = TrackChanges()

class Category(models.Model):
    a = models.CharField(max_length=200)

class M14ManyToMany(models.Model):
    a = models.TextField()
    b = models.ManyToManyField(Category)

    history = TrackChanges()

class LongerNameOfThing(models.Model):
    a = models.TextField()

    history = TrackChanges()

class M15OneToOne(models.Model):
    a = models.CharField(max_length=200)
    b = models.OneToOneField(LongerNameOfThing)

    history = TrackChanges()

class M16Unique(models.Model):
    a = models.CharField(max_length=200, unique=True)
    b = models.TextField()
    c = models.IntegerField()

    history = TrackChanges()

class M17ForeignKeyVersioned(models.Model):
    name = models.CharField(max_length=200)
    m2 = models.ForeignKey(M2)

    history = TrackChanges()

class M17ForeignKeyVersionedCustom(models.Model):
    name = models.CharField(max_length=200)
    m2 = models.ForeignKey(M2)

    history = TrackChanges()

class M18OneToOneFieldVersioned(models.Model):
    name = models.CharField(max_length=200)
    m2 = models.OneToOneField(M2)

    history = TrackChanges()

class LameTag(models.Model):
    name = models.CharField(max_length=200)

    history = TrackChanges()

class M19ManyToManyFieldVersioned(models.Model):
    a = models.TextField()
    tags = models.ManyToManyField(LameTag)

    history = TrackChanges()

class CustomManager(models.Manager):
    def foo(self):
        print "bar"

class M20CustomManager(models.Model):
    name = models.CharField(max_length=200)
    objects = models.Manager()

    myman = CustomManager()
    
    history = TrackChanges()

class M21CustomAttribute(models.Model):
    name = models.CharField(max_length=200)
    magic = "YES"

    history = TrackChanges()

TEST_MODELS = [
    M1, M2, M3BigInteger, M4Date, M5Decimal, M6Email, M7Numbers,
    M8Time, M9URL, M10File, M11Image, M12ForeignKey, M13ForeignKeySelf,
    M14ManyToMany, M15OneToOne, M16Unique, M17ForeignKeyVersioned,
    M18OneToOneFieldVersioned, M19ManyToManyFieldVersioned,
    M20CustomManager, M21CustomAttribute,
]
