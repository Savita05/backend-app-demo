from django.conf.urls import url
from django.urls import path
from .views import *
from createuser import views 
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
url(r'registration/$', RegisterUser.as_view()),
url(r'deleterecords/$', Deleterecords.as_view()),
url(r'getuser/$', Getuser.as_view()),
url(r'updateuser/([0-9])$', Updateuser.as_view()),
url(r'loginuser/$', Login.as_view()),
url(r'taskfileslist/$', TaskFiles.as_view()),
url(r'getTaskFilesList/$', GetTaskFilesList.as_view()),
#url(r'userroles/$', UserRoles.as_view()),
url(r'objectlevel/$', ObjectLevel.as_view()),
url(r'getObjectlevel/$', GetObjectLevel.as_view()),
url(r'scenelevel/$', SceneLevelQuery.as_view()),
url(r'getScenelevel/$', GetSceneLevel.as_view()),
url(r'addProjectFiles/$', AddProjectFiles.as_view()),
url(r'getProjectFiles/$', GetAllProjectsDetails.as_view()),
url(r'getProjectFilesname/$', GetProjectName.as_view()),
url(r'getProjectFilesdetails/(?P<project_name>)$', views.getProjectDetails),
url(r'gettaskfilesfilteredonprojects/(?P<project_name>)$', views.gettasksfilteredonProjects),
# ... previously added endpoints
url(r'objectCategories/$', views.getobjectCategories),
url(r'objectcategorieswithid/(?P<pk>[0-9]+)$', views.getobjectCategories_id),
url(r'getAnnotationImageFile/(?P<File_Name>)(?P<project_name>)$', views.getAnnotationImageFile),

url(r'uploadAnnotationimages/', views.uploadimages)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)