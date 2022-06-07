from urllib import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from dayCareApp.models import Parents,Children,ChildrensWork,Events,EventRegisteration,Employee
from dayCareApp.serializers import ParentsSerializers,ChildrensSerializers,ChildrensWorkSerializers,EventsSerializers,EventRegisterationSerializers,EmployeeSerializers
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def loginApi(request):
    if request.method=='GET':
        # Get the email and password
        email = request.GET['Email']
        password = request.GET['Password']

        match_event = Events.objects.last()
        events_serializer = EventsSerializers(match_event)
        
        if not match_event is None:
            match_event_registeration = EventRegisteration.objects.all().filter(EventId = events_serializer.data['EventId'])
            
            # Check to see if any Parents already exist with this email and password.
            try:
                match = Parents.objects.get(Email=email,Password=password)
                parents_serializer = ParentsSerializers(match)
                if match_event_registeration.exists():
                    return JsonResponse({'status':200,'message':'Logged in Successfully','parentsData':parents_serializer.data,'eventsData':''},safe=False)
                return JsonResponse({'status':200,'message':'Logged in Successfully','parentsData':parents_serializer.data,'eventsData':events_serializer.data},safe=False)
            except Parents.DoesNotExist:
                # Unable to find a user, this is fine
                return JsonResponse({'status':400,'message':'Invalid Credentials.','parentsData':''},safe=False)
                
        try:
            match = Parents.objects.get(Email=email,Password=password)
            parents_serializer = ParentsSerializers(match)
            return JsonResponse({'status':200,'message':'Logged in Successfully','parentsData':parents_serializer.data,'eventsData':''},safe=False)
        except Parents.DoesNotExist:
            return JsonResponse({'status':400,'message':'Invalid Credentials.','parentsData':''},safe=False) 

@csrf_exempt
def signupApi(request):
    if request.method=='POST':
        jsonInput = JSONParser().parse(request)
        email = jsonInput['Email']

        try:
            match = Parents.objects.get(Email=email)
            parents_serializer = ParentsSerializers(match)
            return JsonResponse({'status':400,'message':'Parent already registered with given Email.','parentsData':''},safe=False)
        except Parents.DoesNotExist:
            parents_data=jsonInput
            parents_serializer=ParentsSerializers(data=parents_data)
            if parents_serializer.is_valid():
                parents_serializer.save()
                return JsonResponse({'status':200,'message':'Parent Registered Successfully.','parentsData':parents_serializer.data},safe=False)
            else:
                return JsonResponse({'status':400,'message':'Something went wrong. Please try again.','parentsData':''},safe=False)


@csrf_exempt
def employeeLoginApi(request):
    if request.method=='GET':
        # Get the email and password
        email = request.GET['Email']
        password = request.GET['Password']

        # Check to see if any Parents already exist with this email and password.
        try:
            match = Employee.objects.get(Email=email,Password=password)
            employee_serializer = EmployeeSerializers(match)
            return JsonResponse({'status':200,'message':'Logged in Successfully','employeeData':employee_serializer.data},safe=False)
        except Employee.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'Invalid Credentials.','employeeData':''},safe=False)


@csrf_exempt
def employeeSignupApi(request):
    if request.method=='POST':
        jsonInput = JSONParser().parse(request)
        email = jsonInput['Email']

        try:
            match = Employee.objects.get(Email=email)
            employee_serializer = EmployeeSerializers(match)
            return JsonResponse({'status':400,'message':'Employee already registered with given Email.','employeeData':''},safe=False)
        except Employee.DoesNotExist:
            employee_data=jsonInput
            employee_serializer=EmployeeSerializers(data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse({'status':200,'message':'Employee Registered Successfully.','employeeData':employee_serializer.data},safe=False)
            else:
                return JsonResponse({'status':400,'message':'Something went wrong. Please try again.','employeeData':''},safe=False)


@csrf_exempt
def addChildrenApi(request):
    if request.method=='POST':
        children_data=JSONParser().parse(request)
        childrens_serializer=ChildrensSerializers(data=children_data)
        if childrens_serializer.is_valid():
            childrens_serializer.save()
            return JsonResponse({'status':200,'message':'Child Added Successfully.','childrenData':childrens_serializer.data},safe=False)
        return JsonResponse({'status':400,'message':'Failed to Add Child. Please try again.','childrenData':''},safe=False)

@csrf_exempt 
def getChildrenById(request,id=0):
    if request.method=='GET':
        # Check to see if any children exist with this id.
        try:
            match = Children.objects.get(ChildId=id)
            children_serializer = ChildrensSerializers(match)
            return JsonResponse({'status':200,'message':'Child data found.','childrenData':children_serializer.data},safe=False)
        except Children.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'Child data not found.','childrenData':''},safe=False)

@csrf_exempt 
def getAllChildrenByParentId(request,id=0):
    if request.method=='GET':
        # Check to see if any children exist with this id.
        try:
            match = Children.objects.all().filter(ParentId=id)
            children_serializer = ChildrensSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Childrens data found.','childrenData':children_serializer.data},safe=False)
        except Children.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Child data found.','childrenData':''},safe=False)


@csrf_exempt
def addEventApi(request):
    if request.method=='POST':
        event_data=JSONParser().parse(request)
        events_serializer=EventsSerializers(data=event_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse({'status':200,'message':'Event Added Successfully.','childrenData':events_serializer.data},safe=False)
        return JsonResponse({'status':400,'message':'Failed to Add Event. Please try again.','childrenData':''},safe=False)
 
@csrf_exempt
def getAllEventsApi(request):
    if request.method == 'GET':
        try:
            match = Events.objects.all()
            events_serializer = EventsSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Events data found.','eventsData':events_serializer.data},safe=False)
        except Events.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Events data found.','userData':''},safe=False)

@csrf_exempt
def getEventByIdApi(request,id=0):
    if request.method == 'GET':
        try:
            match = Events.objects.all().filter(EventId = id)
            events_serializer = EventsSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Events data found.','eventsData':events_serializer.data},safe=False)
        except Events.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Events data found.','eventsData':''},safe=False)

@csrf_exempt
def approvalUserUpdateApi(request):
    if request.method == 'PUT' :
        parents_data=JSONParser().parse(request)
        parents=Parents.objects.get(ParentId=parents_data['ParentId'])
        parents_serializer=ParentsSerializers(parents,data=parents_data)
        if parents_serializer.is_valid():
            parents_serializer.save()
            return JsonResponse({'status':200,'message':"Approval updated Successfully.",'parentsData':parents_serializer.data},safe=False)
        return JsonResponse({'status':400,'message':'Failed to update approval.','parentsData':''},safe=False)

@csrf_exempt
def eventRegisterationApi(request):
    if request.method == 'POST':
        event_registeration_data=JSONParser().parse(request)
        event_registeration_serializer=EventRegisterationSerializers(data=event_registeration_data)
        if event_registeration_serializer.is_valid():
            event_registeration_serializer.save()
            return JsonResponse({'status':200,'message':'Registered for the Event Successfully.','eventRegisterationData':event_registeration_serializer.data},safe=False)
        return JsonResponse({'status':400,'message':'Failed to Register for the event. Please try again.','eventRegisterationData':''},safe=False)

@csrf_exempt
def getUserRegisteredEventApi(request,id=0):
    if request.method == 'GET':
        try:
            match = EventRegisteration.objects.all().filter(ParentId = id)
            events_serializer = EventRegisterationSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Registered Events data found.','eventsData':events_serializer.data},safe=False)
        except EventRegisteration.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Registered Events data found.','eventsData':''},safe=False)

@csrf_exempt
def addChildrensWorkApi(request):
    if request.method == 'POST':
        docPath=request.FILES['DocPath']
        childId=request.POST['ChildId']
        dateOfSubmission=request.POST['DateOfSubmission']

        file_name=default_storage.save(docPath.name,docPath)

        request_data = {
            'DocPath':file_name,
            'ChildId':childId,
            'DateOfSubmission':dateOfSubmission
        }
        
        childrens_work_serializer=ChildrensWorkSerializers(data=request_data)
        if childrens_work_serializer.is_valid():
            childrens_work_serializer.save()
            return JsonResponse({'status':200,'message':'Word of the children added Successfully.','childrensWorkData':childrens_work_serializer.data},safe=False)
        return JsonResponse({'status':400,'message':'Failed to add childrens work. Please try again.','childrensWorkData':''},safe=False)

@csrf_exempt
def getChildrenWorkByChildrenIdApi(request,id=0):
    if request.method == 'GET':
        try:
            match = ChildrensWork.objects.all().filter(ChildId = id)
            events_serializer = ChildrensWorkSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Childrens work data found.','childrensWorkData':events_serializer.data},safe=False)
        except ChildrensWork.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Word data found.','childrensWorkData':''},safe=False)

@csrf_exempt
def getEventByParentIdApi(request,id=0):
    if request.method == 'GET':
        try:
            match = Events.objects.all()
            events_serializer = EventsSerializers(match,many=True)
            all_result = list(events_serializer.data)
            for results in all_result:   #Iterate over members
                match_event_registeration = EventRegisteration.objects.all().filter(EventId = results['EventId'],ParentId = id)
                if match_event_registeration.exists():
                    results['status'] = 1
                else:
                    results['status'] = 0
            return JsonResponse({'status':200,'message':'Events data found.','eventsData':all_result},safe=False)
        except Events.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Events data found.','eventsData':''},safe=False)

@csrf_exempt 
def getAllEventsRegisteredApi(request):
    if request.method == 'GET':
        try:
            match = EventRegisteration.objects.all()
            events_serializer = EventRegisterationSerializers(match,many=True)
            all_result = list(events_serializer.data)
            for results in all_result:   
                match_parent = Parents.objects.get(ParentId=results['ParentId'])
                parents_serializer = ParentsSerializers(match_parent)
                results['parentsData'] = parents_serializer.data
            return JsonResponse({'status':200,'message':'Registered Events data found.','eventsData':all_result},safe=False)
        except EventRegisteration.DoesNotExist:
            return JsonResponse({'status':400,'message':'No Registered Events data found.','eventsData':''},safe=False)

@csrf_exempt
def getAllParentsApi(request):
    if request.method == 'GET':
        try:
            match = Parents.objects.all()
            parents_serializer = ParentsSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Child data found.','parentsData':parents_serializer.data},safe=False)
        except Children.DoesNotExist:
            return JsonResponse({'status':400,'message':'Child data not found.','parentsData':''},safe=False)

@csrf_exempt
def getAllChildrenApi(request):
    if request.method=='GET':
        # Check to see if any children exist with this id.
        try:
            match = Children.objects.all()
            children_serializer = ChildrensSerializers(match,many=True)
            return JsonResponse({'status':200,'message':'Childrens data found.','childrenData':children_serializer.data},safe=False)
        except Children.DoesNotExist:
            # Unable to find a user, this is fine
            return JsonResponse({'status':400,'message':'No Child data found.','childrenData':''},safe=False)

@csrf_exempt
def getEventByRegisteredEventApi(request,id=0):
    if request.method == 'GET':
        try:
            match = EventRegisteration.objects.all().filter(EventId = id)
            events_serializer = EventRegisterationSerializers(match,many=True)
            all_result = list(events_serializer.data)
            for results in all_result:   
                match_parent = Parents.objects.get(ParentId=results['ParentId'])
                parents_serializer = ParentsSerializers(match_parent)
                results['parentsData'] = parents_serializer.data
            return JsonResponse({'status':200,'message':'Registered Events data found.','eventsData':all_result},safe=False)
        except EventRegisteration.DoesNotExist:
            return JsonResponse({'status':400,'message':'No Registered Events data found.','eventsData':''},safe=False)