from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,
                                   null=True)
    def __str__(self):
        return self.name
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, related_name="measurements", on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.temperature}, {self.created_at}'