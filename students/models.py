from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser



LEANER=10
THINKER=20
HACKER=30
ENGINEER=40
EXPERT=50

LEVEL_CHOICES=(
    (LEANER,'LEANER'), (THINKER,"THINKER"), (HACKER,"HACKER",), (ENGINEER,"ENGINEER",), (EXPERT,"EXPERT")
)

STAGE_1=1
STAGE_2=2
STAGE_3=3

STAGE_CHOICES=(
    (STAGE_1,"Stage 1"), (STAGE_2,"Stage 2"), (STAGE_3,"Stage 3")
)

ONE=1
TWO=2
THREE=3
FOUR=4
FIVE=5
SIX=6
SIVEN=7
EIGHT=8
NINE=9
TEN=10

AVERAGE_SCORE_CHOICES=(
    (ONE,"1"),(TWO,"2"),(THREE,"3"),(FOUR,"4"),(FIVE,"5"),(SIX,"6"),(SIVEN,"7"),(EIGHT,"8"),(NINE,"9"),(TEN,"10"),
)




class Student(AbstractUser):
    cohort=models.CharField(max_length=10,null=True,blank=True,default="19.2")
    updated_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        if self.first_name:
          return ("{}".format(self.first_name))
        else:
            return ("{} - Admin".format(self.username))




class Hardware_iot(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="Hd")
    stage=models.IntegerField(choices=STAGE_CHOICES,default=0,null=True,blank=True)
    electronics_circuit_design = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    pcb_designing = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    embedded_hardware_platform = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    sensors_actuators = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    modules_integrations = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    system_interfaces_implementation = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    data_acquisition_techniques = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    basic_of_networking = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    power_design_for_circuits = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating=models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage="Stage 0"
        if self.stage==1:
            stage="Stage 1"
        if self.stage == 2:
                stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"

        return ("{} - Hardware & Iot - {} ".format(self.student.first_name,stage))

class Ai(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="Ai")
    stage = models.IntegerField(choices=STAGE_CHOICES, default=0, null=True, blank=True)
    data_modelling_evaluation = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    probablity_statistics = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    applied_math_algorithms = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    applied_machine_learning = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    distributed_computing = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    edge_computing = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{} - AI/ML - {} ".format(self.student.first_name,stage))


class Software(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="S")
    stage=models.IntegerField(choices=STAGE_CHOICES,default=0,null=True,blank=True)
    Linux_mac_packaging = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    cloud_platform = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    web_application_development = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    mobile_application_development = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    application_architecture_design = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{} - Application Development - {}".format(self.student.first_name,stage))


class Product_design(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="Pd")
    stage = models.IntegerField(choices=STAGE_CHOICES, default=0, null=True, blank=True)
    rapid_prototyping = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    principles_of_industrial_design = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    ui_ux_Design = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    cad = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    analysis_of_mechanical_design = models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{} - Product/Industrial Design - {}".format(self.student.first_name,stage))



class Software_platforms(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="Sp")
    stage = models.IntegerField(choices=STAGE_CHOICES, default=0, null=True, blank=True)
    eagle_pcb=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    psim_multi_sim=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    lab_view= models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    matlab=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    tableau=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    tibco_spotfire=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{} - Software Platform - {}".format(self.student.first_name,stage))





class Programming(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="P")
    stage=models.IntegerField(choices=STAGE_CHOICES,default=0,null=True,blank=True)
    defining_problem=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    computer_science_fundamentals=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    programming_techniques=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    programming_languages=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{} - Programming - {}".format(self.student.first_name,stage))


class Intellectual_Property(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="Ip")
    stage = models.IntegerField(choices=STAGE_CHOICES, default=0, null=True, blank=True)
    ip_exploration=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    patent_drafting=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    key_word_seaching=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES,default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{} - IPR - {}".format(self.student.first_name,stage))

class Innovation(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="I")
    stage=models.IntegerField(choices=STAGE_CHOICES,default=0,null=True,blank=True)
    problem_validation=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    customer_development=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    testing_value_proposition=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    solution_alternatives_exploration=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    pitch=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    grant_proposal_writing=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    milestones_planning_reporting=models.IntegerField(choices=LEVEL_CHOICES,default=0, null=True, blank=True)
    rating = models.IntegerField(choices=AVERAGE_SCORE_CHOICES, default=0, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        stage = "Stage 0"
        if self.stage == 1:
            stage = "Stage 1"
        if self.stage == 2:
            stage = "Stage 2"
        if self.stage == 3:
            stage = "Stage 3"
        return ("{}-Innovation - {}".format(self.student.first_name,stage))