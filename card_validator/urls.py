from card_validator import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from django.urls import path


urlpatterns = [
    path('cards/', views.CardNumberList.as_view()),
    path('cards/<str:num>/', views.CardNumberDetail.as_view()),
    path('openapi/', get_schema_view(
        title="Card validation service",
        description="API developers hoping to use our service"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
