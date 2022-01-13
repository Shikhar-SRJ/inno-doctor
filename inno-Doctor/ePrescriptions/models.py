from django.db import models

# Create your models here.
class InternationalPatientSummary(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    gender = models.CharField(max_length=100, null=False, blank=False)
    aadhar_no = models.IntegerField(unique=True, null=False, blank=False)
    
    
    # class Meta:
    #     app_label = 'InternationalPatientSummary'

class ProblemList(models.Model):
    id = models.IntegerField(primary_key=True)
    ips = models.ForeignKey(
        InternationalPatientSummary, on_delete=models.CASCADE
    )
    problem = models.CharField(max_length=250, null=False, blank=False)
    body_site = models.CharField(max_length=300, null=False, blank=False)
    severity = models.CharField(max_length=100)
    onset_date = models.DateField(auto_now=True)
    abatement_date = models.DateField()
    diagnostic_certainty = models.CharField(max_length=200)
    # class Meta:
    #     app_label = 'ProblemList'

class VitalSigns(models.Model):
    id = models.IntegerField(primary_key=True)
    ips = models.ForeignKey(
        InternationalPatientSummary, on_delete=models.CASCADE
    )
    body_weight = models.FloatField()
    height = models.FloatField()
    respiration_rate = models.FloatField()
    pulse_rate = models.FloatField()
    body_temperature = models.FloatField()
    head_circumference = models.FloatField()
    pulse_oximetry = models.FloatField()
    body_mass_index = models.FloatField()
    blood_pressure_systolic = models.FloatField()
    blood_pressure_diastolic = models.FloatField()
    # class Meta:
    #     app_label = 'VitalSigns'

class SocialHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    ips = models.ForeignKey(
        InternationalPatientSummary, on_delete=models.CASCADE
    )
    tobacco_smoking_status = models.CharField(max_length=50)
    alcohol_consumption_status = models.CharField(max_length=50)
    alcohol_consumption_unit = models.IntegerField()
    alcohol_consumption_frequency = models.CharField(max_length=100)
    # class Meta:
    #     app_label = 'SocialHistory'

class MedicationStatement(models.Model):
    id = models.IntegerField(primary_key=True)
    ips = models.ForeignKey(InternationalPatientSummary, on_delete=
    models.CASCADE)
    medication_item = models.CharField(max_length=200, null=False,
                                       blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    form = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    unit_of_prescription = models.CharField(
        max_length=100, null=False, blank=False
    )
    batch_id = models.CharField(max_length=100, null=False, blank=False)
    expiry = models.DateField(null=False, blank=False)
    dose_amount = models.FloatField(null=False, blank=False)
    dose_duration = models.CharField(
        max_length=100, null=False, blank=False
    )
    dose_unit = models.CharField(max_length=100, null=False, blank=False)
    dose_frequency = models.CharField(
        max_length=100, null=True, blank=True
    )
    dose_interval = models.CharField(
        max_length=100, null=True, blank=True
    )
    dose_specific_timing = models.TimeField()
    route = models.CharField(max_length=100, null=False, blank=False)
    body_site = models.CharField(max_length=100, null=False, blank=False)
    # class Meta:
    #     app_label = 'MedicationStatement'

class EPrescription(models.Model):
    id = models.IntegerField(primary_key=True)
    ips = models.ForeignKey(InternationalPatientSummary, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    # class Meta:
    #     app_label = 'EPrescription'

class MedicationOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    eprescription = models.ForeignKey(EPrescription, on_delete=models.CASCADE)
    medication_item = models.CharField(max_length=200, null=False, blank=False)
    route = models.CharField(max_length=100, null=False, blank=False)
    dosage_instructions = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    # class Meta:
    #     app_label = 'MedicationOrder'
class DosageInstructions(models.Model):
    id = models.IntegerField(primary_key=True)
    medication_order = models.ForeignKey(MedicationOrder, on_delete=models.CASCADE)
    dose_amount = models.FloatField(null=False, blank=False)
    dose_duration = models.CharField(max_length=100, null=False, blank=False)
    dose_unit = models.CharField(max_length=100, null=False, blank=False)
    dose_frequency = models.CharField(max_length=100, null=True, blank=True)
    dose_interval = models.CharField(max_length=100, null=True, blank=True)
    dose_specific_timing = models.TimeField()
    # class Meta:
    #     app_label = 'DosageInstructions'