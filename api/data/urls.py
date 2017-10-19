from django.conf.urls import include, url
from rest_framework import routers

from data import views

router = routers.SimpleRouter()
router.register(r'investment', views.InvestmentViewSet, 'investment')
router.register(r'year', views.YearViewSet, 'year')
router.register(r'sector', views.SectorViewSet, 'sector')
router.register(r'program', views.ProgramViewSet, 'program')
router.register(r'rec', views.RecViewSet, 'rec')
router.register(r'sit', views.SitViewSet, 'sit')
router.register(r'source', views.SourceViewSet, 'source')


urlpatterns = [
    url(r'^', include(router.urls)),
]
