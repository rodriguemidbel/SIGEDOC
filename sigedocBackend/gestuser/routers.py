from rest_framework.routers import DefaultRouter
from .views import *
from gestuser import views

router = DefaultRouter()
#____________________URLs___________________________________________________
router.register('usergroups', UsergroupViewset, basename='usergroups')
router.register('users', UserViewset, basename='users')
router.register('logs', LogViewset, basename='logs')
router.register('features', FeatureViewset, basename='features')
router.register('privileges', PrivilegeViewset, basename='privileges')
#____________________End URL_______________________________________________
urlpatterns= router.urls