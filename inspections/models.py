from django.db import models
import uuid


class Facility(models.Model):
    facility_name = models.CharField(max_length=50)
    facility_type = models.CharField(max_length=50, blank=True)
    facility_address = models.CharField(max_length=200, blank=True)
    facility_city = models.CharField(max_length=25, blank=True)
    facility_uuid = models.UUIDField(unique=True)

    def __str__(self):
        return "%s %s" (self.facility_name, self.facility_city)

    class Meta:
        verbose_name_plural = "Facilities"


class Inspection(models.Model):
    facility = models.ForeignKey(Facility, to_field="facility_uuid", on_delete="cascade")
    inspect_date = models.DateField()
    inspect_type = models.CharField(max_length=40, blank=True)
    inspect_result = models.CharField(max_length=20, blank=True)
    critical = models.IntegerField()
    non_critical = models.IntegerField()
    total_points = models.IntegerField()
    inspect_details = models.TextField(blank=True)


