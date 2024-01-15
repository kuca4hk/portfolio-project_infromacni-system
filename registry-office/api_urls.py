from rest_framework.routers import DefaultRouter
from django.urls import include, path, re_path
# from demo_app.apps.TodoDemo.views import TodoViewSet
from .apps.organizations.views import OrganizationViewSet, VirtualOperationViewSet
from .apps.users.views import PersonDetailViewSet, PersonDetailViewSetAll
from .apps.scholl_class.views import ClassViewSet, DetailClassViewSet, StudentDetailViewSet, StudentDetailViewSetAll, DownloadTempleta, ExportClass

router = DefaultRouter()
# router.register(r'todos', TodoViewSet, basename='todos')
router.register(r'organizations', OrganizationViewSet, basename='organizations')
router.register(r'virtual-operations', VirtualOperationViewSet, basename='virtual-operations')
# router.register(r'persons', PersonViewSet, basename='persons')
router.register(r'person-details', PersonDetailViewSetAll, basename='person-details')
router.register(r'classes', ClassViewSet, basename='classes')
# router.register(r'students', StudentViewSet, basename='students')
router.register(r'student-details', StudentDetailViewSetAll, basename='student-details')
# router.register(r'study-fields', StudyFieldViewSet, basename='study-fields')

urlpatterns = [
    # ...
    path('classess/<str:class_name>/', DetailClassViewSet.as_view({'get': 'retrieve'}), name='class-detail'),
    path('person-details/<str:student_surname>/', PersonDetailViewSet.as_view({'get': 'retrieve'}), name='person-detail'),
    path('student-details/<str:student_surname>/', StudentDetailViewSet.as_view({'get': 'retrieve'}), name='student-detail'),
    path('download-template-xlsx/', DownloadTempleta.as_view(), name='download-template-xlsx'),
    path("download-classes-xlsx/<str:class_name>/", ExportClass.as_view(), name="download-classes-xlsx"),
    # ...
]

urlpatterns += router.urls
