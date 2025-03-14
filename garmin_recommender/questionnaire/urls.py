from django.urls import path
from .views import dashboard, questionnaire_view, watch_catalog, compare_watches

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("questionnaire/", questionnaire_view, name="questionnaire"),
    path("catalog/", watch_catalog, name="watch_catalog"),
    path("compare/", compare_watches, name="compare_watches"),
]
