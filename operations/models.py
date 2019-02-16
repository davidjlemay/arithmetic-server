from django.db import models

# Create your models here.

class Objective(models.Model):
  def __str__(self):
    return self.objective_text
  name = models.CharField(max_length=50)
  topic = models.CharField(max_length=50)
  objective_text = models.CharField(max_length=200) 

class Question(models.Model):
  def __str__(self):
    return self.question_text
  objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
  question_text = models.CharField(max_length=200)

class Term(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  coefficient = models.DecimalField(max_digits=5, decimal_places=0)
  numerator = models.DecimalField(max_digits=5, decimal_places=0)
  denominator = models.DecimalField(max_digits=5, decimal_places=0)
  exponent = models.DecimalField(max_digits=1, decimal_places=0)

class Formula_Parameters(models.Model):
  objective = models.ForeignKey(Objective, on_delete=models.CASCADE)
  coefficient = models.BooleanField()
  numerator = models.BooleanField()
  denominator = models.BooleanField()
  exponent = models.BooleanField()
