from django.urls import include,path
from dayCareApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login/', views.loginApi),
    path('signup/', views.signupApi),
    path('employeeLogin/', views.employeeLoginApi),
    path('employeeSignup/', views.employeeSignupApi),
    path('addChildren/',views.addChildrenApi),
    path('getChildrenById/<int:id>/',views.getChildrenById),
    path('getAllChildren/<int:id>/',views.getAllChildrenByParentId),
    path('addEvent/',views.addEventApi),
    path('getAllEvents/',views.getAllEventsApi),
    path('getEventById/<int:id>/',views.getEventByIdApi),
    path('approvalUserUpdate/',views.approvalUserUpdateApi),
    path('eventRegisteration/',views.eventRegisterationApi),
    path('getUserRegisteredEvent/<int:id>/',views.getUserRegisteredEventApi),
    path('addChildrensWork/',views.addChildrensWorkApi),
    path('getChildrenWorkByChildrenId/<int:id>/',views.getChildrenWorkByChildrenIdApi),
    path('getEventByParentId/<int:id>',views.getEventByParentIdApi),
    path('getAllEventsRegistered/',views.getAllEventsRegisteredApi),
    path('getAllParents/',views.getAllParentsApi),
    path('getAllChildren/',views.getAllChildrenApi),
    path('getEventByRegisteredEvent/<int:id>/',views.getEventByRegisteredEventApi),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

