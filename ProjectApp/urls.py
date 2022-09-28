import imp
from django.urls import path,re_path
from ProjectApp  import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r"department", views.departmentApi),
    re_path(r"^department/([0-9]+)$",views.departmentApi),
    path(r"employee", views.employeeApi),
    re_path(r"^employee/([0-9]+)$",views.employeeApi),

    path(r"employee/savefile", views.saveFile)

]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)