from rest_framework import serializers
from dayCareApp.models import Parents,Children,ChildrensWork,Events,EventRegisteration,Employee

class ParentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields=('ParentId','FirstName','LastName','SpouseFirstName','SpouseLastName','Street','State','City','Zipcode','Email','PhoneNumber','Password','NumberOfChildren','BalanceDue','DateOfJoining','ApprovalStatus')

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields=('EmployeeId','FirstName','LastName','Street','State','City','Zipcode','Email','PhoneNumber','Password')

class ChildrensSerializers(serializers.ModelSerializer):
    class Meta:
        model = Children
        fields=('ChildId','ParentId','FirstName','LastName','ParentFirstName','ParentLastName','Age')        

class ChildrensWorkSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChildrensWork
        fields=('WorkId','ChildId','DocPath','DateOfSubmission')

class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields=('EventId','EventsName','EventDate','EventTime','EventsAddress','EventsCost','EventsSafety')

class EventRegisterationSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventRegisteration
        fields=('RegisterationId','ParentId','EventId','ParentsCountComing','RegisterationDate')
