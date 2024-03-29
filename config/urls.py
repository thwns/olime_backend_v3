"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from strawberry.django.views import GraphQLView
from .schema import schema
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/v1/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    #path("api/v1/contents/", include("contents.urls")),
    #path("api/v1/tasks/", include("tasks.urls")),
    #path("api/v1/categories/", include("categories.urls")),
    #path("api/v1/medias/", include("medias.urls")),
    #path("api/v1/followings/", include("followings.urls")),
    #path("api/v1/lovings/", include("lovings.urls")),
    #path("api/v1/followlists/", include("followlists.urls")),
    path("api/v1/users/", include("users.urls")),
    #path("api/v1/reviews/", include("reviews.urls")),
    #path("api/v1/replys/", include("replys.urls")),
    path("api/v1/performances/", include("performances.urls")),
    path("api/v1/workbooks/", include("workbooks.urls")),
    path("api/v1/workbook_evaluations/", include("workbook_evaluations.urls")),
    path("api/v1/schools/", include("schools.urls")),
    #path("api/v1/subjects/", include("subjects.urls")),
    path("api/v1/current_schools/", include("current_schools.urls")),
    path("api/v1/target_schools/", include("target_schools.urls")),
    path("api/v1/early_decisions/", include("early_decisions.urls")),
    path("api/v1/regular_decisions/", include("regular_decisions.urls")),
    path("api/v1/task_days/", include("task_days.urls")),
    path("api/v1/task_guidelines/", include("task_guidelines.urls")),
    path("api/v1/task_personals/", include("task_personals.urls")),
    path("api/v1/difficult_questions/", include("difficult_questions.urls")),
    path("api/v1/task_evaluations/", include("task_evaluations.urls")),
    path("api/v1/task_assignments/", include("task_assignments.urls")),
    path("graphql", GraphQLView.as_view(schema=schema)),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^user-uploads/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
