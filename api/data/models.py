from django.db import models
from django.utils.translation import ugettext as _


class Year(models.Model):
    """Year model

    Atributes db:
        - year: year of the investment
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """

    year = models.CharField(max_length=4, verbose_name=_('year'))
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('year')
        verbose_name_plural = _('years')

    def __str__(self):
        return self.year


class Sector(models.Model):
    """Sector model

    Atributes db:
        - code: code of the sector
        - name: name of the sector
        - unit: unit execting oh the sector
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """
    code = models.IntegerField(verbose_name=_('code'))
    name = models.CharField(max_length=300, verbose_name=_('name'))
    unit = models.CharField(max_length=300, verbose_name=_('executing unit'))
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('sector')
        verbose_name_plural = _('sectors')

    def __str__(self):
        return self.code


class Program(models.Model):
    """Program model

    Atributes db:
        - prog: id of the program
        - subp: id of the sub program
        - proy: id of the proyect
        - subpr: id of the sub proyect
        - name: name of the investment
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """
    prog = models.IntegerField(verbose_name=_('program'))
    subp = models.IntegerField(verbose_name=_('sub program'))
    proy = models.IntegerField(verbose_name=_('proyect'))
    subpr = models.IntegerField(verbose_name=_('sub proyect'))
    name = models.CharField(max_length=300, verbose_name=_('name'))
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('program')
        verbose_name_plural = _('programs')

    def __str__(self):
        return self.prog


class Rec(models.Model):
    """Rec model

    Atributes db:
        - rec: rec of the investment
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """

    rec = models.IntegerField(verbose_name=_('rec'))
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('rec')
        verbose_name_plural = _('rec')

    def __str__(self):
        return self.rec


class Sit(models.Model):
    """Sit model

    Atributes db:
        - sit: sit of the investment
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """

    sit = models.CharField(max_length=1, verbose_name=_('sit'))
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('sit')
        verbose_name_plural = _('sit')

    def __str__(self):
        return self.sit


class Source(models.Model):
    """Source model

    Atributes db:
        - name: name of the source
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """

    name = models.CharField(max_length=50, verbose_name=_('source'))
    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('source')
        verbose_name_plural = _('sources')

    def __str__(self):
        return self.name


class Investment(models.Model):
    """Investment model

    Atributes db:
        - approval_init: aproval init of the investment
        - approval_current: aproval current of the investment
        - commitments: commitments of the investment
        - obligations: obligations of the investment
        - payments: payments of the investment
        - created_at: date the object is created (Automatically generated).
        - updated_at: date the object is updated (Automatically generated and updated).
    """
    year = models.ForeignKey(Year, verbose_name=_('year'))
    sector = models.ForeignKey(Sector, verbose_name=_('sector'))
    program = models.ForeignKey(Program, verbose_name=_('program'))
    sit = models.ForeignKey(Sit, verbose_name=_('sit'))
    rec = models.ForeignKey(Rec, verbose_name=_('rec'))
    source = models.ForeignKey(Source, verbose_name=_('source'))

    approval_init = models.CharField(max_length=50, verbose_name=_('approval init'))
    approval_current = models.CharField(max_length=50, verbose_name=_('approval current'))
    commitments = models.CharField(max_length=50, verbose_name=_('commitments'))
    obligations = models.CharField(max_length=50, verbose_name=_('obligations'))
    payments = models.CharField(max_length=50, verbose_name=_('payments'))

    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False)
    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False)

    class Meta:
        verbose_name = _('investment')
        verbose_name_plural = _('investment')
