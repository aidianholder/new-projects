from django.db import models
import uuid
from decimal import Decimal


class Facility(models.Model):
    facility_name = models.CharField(max_length=50)
    facility_type = models.CharField(max_length=50, blank=True)
    facility_address = models.CharField(max_length=200, blank=True)
    facility_city = models.CharField(max_length=25, blank=True)
    facility_uuid = models.UUIDField(unique=True)

    def __str__(self):
        return "{0}{1}".format(self.facility_name, self.facility_city)

    def pass_fail_total(self):
        all_inspections = self.inspection_set.all()
        passed = Decimal(0)
        failed = Decimal(0)
        for event in all_inspections:
            if event.passed_or_failed() == 'passed':
                passed += 1
            if event.passed_or_failed() == 'failed':
                failed += 1
        failed_percent = 100 * (Decimal(failed) / Decimal(failed + passed))
        passed_percent = Decimal(100) - failed_percent
        return {'failed': failed, 'passed': passed, 'failed_percent': failed_percent, 'passed_percent': passed_percent}

    def latest_inspection(self):
        most_recent = self.inspection_set.latest('inspection_date')
        return most_recent.inspection_date

    def assign_uuid(self):
        if not self.facility_uuid:
            working_str = str("{0}{1}".format(self.facility_name.strip(), self.facility_address.strip()))
            self.facility_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, working_str)

    class Meta:
        verbose_name_plural = "Facilities"


class Inspection(models.Model):
    facility = models.ForeignKey(Facility, to_field="facility_uuid", on_delete=models.CASCADE)
    inspect_date = models.DateField()
    inspect_type = models.CharField(max_length=40, blank=True)
    inspect_result = models.CharField(max_length=20, blank=True)
    critical = models.IntegerField()
    non_critical = models.IntegerField()
    total_points = models.IntegerField()
    inspect_details = models.TextField(blank=True)

    def __str__(self):
        return "{0}{1}{2}".format(self.facility.facility_name, self.inspect_type, self.inspect_type)

    def passed_or_failed(self):
        result_cleaned = self.inspect_result.strip().lower()
        if result_cleaned == "failed" or result_cleaned == "re-inspection required" or result_cleaned == "compliance required":
            return 'failed'
        else:
            return 'passed'

    class Meta:
        ordering = ['-inspect_date']
        verbose_name_plural = "Inspections"


