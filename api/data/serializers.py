from rest_framework import serializers

from data import models


class YearSerializer(serializers.ModelSerializer):
    """
        Year Serializer
    """
    class Meta:
        model = models.Year
        fields = ('id', 'year')
        read_only_fields = ('id',)


class SectorSerializer(serializers.ModelSerializer):
    """
        Sector Serializer
    """
    class Meta:
        model = models.Sector
        fields = ('id', 'code', 'name', 'unit')
        read_only_fields = ('id',)


class ProgramSerializer(serializers.ModelSerializer):
    """
        Program Serializer
    """
    class Meta:
        model = models.Program
        fields = ('id', 'prog', 'subp', 'proy', 'subpr', 'name')
        read_only_fields = ('id',)


class RecSerializer(serializers.ModelSerializer):
    """
        Rec Serializer
    """
    class Meta:
        model = models.Rec
        fields = ('id', 'rec')
        read_only_fields = ('id',)


class SitSerializer(serializers.ModelSerializer):
    """
        Rec Serializer
    """
    class Meta:
        model = models.Sit
        fields = ('id', 'sit')
        read_only_fields = ('id',)


class SourceSerializer(serializers.ModelSerializer):
    """
        Source Serializer
    """
    class Meta:
        model = models.Source
        fields = ('id', 'name')
        read_only_fields = ('id',)


class InvestmentSerializer(serializers.ModelSerializer):
    """
        Investment Serializer
    """
    year = YearSerializer()
    sector = SectorSerializer()
    program = ProgramSerializer()
    rec = RecSerializer()
    sit = SitSerializer()
    source = SourceSerializer()

    class Meta:
        model = models.Investment
        fields = (
            'id', 'approval_init', 'approval_current', 'commitments', 'obligations',
            'payments', 'year', 'sector', 'program', 'rec', 'sit', 'source'
        )
        read_only_fields = ('id',)
