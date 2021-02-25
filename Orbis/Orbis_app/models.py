from django.db import models

# Create your models here.
class Essence(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    child = models.OneToOneField('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'essence'

    def __str__(self):
        return self.name

    def get_fields(self):
        if self.child:
            return {"name": self.name, "type": self.type, "child": [self.child.get_fields()]}
        return {"name": self.name, "type": self.type, "child": None}
