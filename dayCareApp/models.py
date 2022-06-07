from django.db import models

# Create your models here.

class Parents(models.Model):
    ParentId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    SpouseFirstName = models.CharField(max_length=500)
    SpouseLastName = models.CharField(max_length=500)
    Street = models.CharField(max_length=500)
    State = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Zipcode = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    PhoneNumber = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    NumberOfChildren = models.IntegerField()
    BalanceDue = models.CharField(max_length=500)
    DateOfJoining = models.CharField(max_length=500)
    ApprovalStatus = models.BooleanField() 

class Employee(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    Street = models.CharField(max_length=500)
    State = models.CharField(max_length=500)
    City = models.CharField(max_length=500)
    Zipcode = models.CharField(max_length=500)
    Email = models.CharField(max_length=500)
    PhoneNumber = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)
    
class Children(models.Model):
    ChildId = models.AutoField(primary_key=True)
    ParentId = models.IntegerField()
    FirstName = models.CharField(max_length=500)
    LastName = models.CharField(max_length=500)
    ParentFirstName = models.CharField(max_length=500)
    ParentLastName = models.CharField(max_length=500)
    Age = models.CharField(max_length=500)
    
class ChildrensWork(models.Model):
    WorkId = models.AutoField(primary_key=True)
    ChildId = models.IntegerField()
    DocPath = models.CharField(max_length=500)
    DateOfSubmission = models.CharField(max_length=500)

class Events(models.Model):
    EventId = models.AutoField(primary_key=True)
    EventsName = models.CharField(max_length=500)
    EventDate = models.CharField(max_length=500)
    EventTime = models.CharField(max_length=500)
    EventsAddress = models.CharField(max_length=1000)
    EventsCost = models.CharField(max_length=1000)
    EventsSafety = models.CharField(max_length=1000)

class EventRegisteration(models.Model):
    RegisterationId = models.AutoField(primary_key=True)
    ParentId = models.IntegerField()
    EventId = models.IntegerField()
    ParentsCountComing = models.IntegerField()
    RegisterationDate = models.CharField(max_length=500)

