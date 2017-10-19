from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from data import models, serializers


class YearViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Year
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('year',)
    queryset = models.Year.objects.all()
    search_fields = ('year')
    serializer_class = serializers.YearSerializer


class SectorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Sector
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('code',)
    queryset = models.Sector.objects.all()
    search_fields = ('code', 'name', 'unit')
    serializer_class = serializers.SectorSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Program
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('prog', 'subp', 'proy', 'subpr')
    queryset = models.Program.objects.all()
    search_fields = ('name')
    serializer_class = serializers.ProgramSerializer


class RecViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Rec
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('rec',)
    queryset = models.Rec.objects.all()
    search_fields = ('rec')
    serializer_class = serializers.RecSerializer


class SitViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Sit
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('sit',)
    queryset = models.Sit.objects.all()
    search_fields = ('sit')
    serializer_class = serializers.SitSerializer


class SourceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Source
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('name',)
    queryset = models.Source.objects.all()
    search_fields = ('name')
    serializer_class = serializers.SourceSerializer


class InvestmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Investment
    """
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('year__year', 'sector__code', 'program__prog')
    queryset = models.Investment.objects.all()
    search_fields = ('year__year', 'sector__code', 'program__name')
    serializer_class = serializers.InvestmentSerializer
