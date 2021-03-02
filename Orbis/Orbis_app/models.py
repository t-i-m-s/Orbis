from django.db import models

# Create your models here.
class Essence(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'essence'

    def __str__(self):
        return self.name

    def get_fields(self):
        if self.essence_set.all():
            return {"name": self.name, "type": self.type, "child": list(map(lambda x: x.get_fields(), self.essence_set.all()))}
        return {"name": self.name, "type": self.type, "child": None}
