import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from data import models


@pytest.fixture
def client():
    """
    Returns APIClient object:
    """
    return APIClient()


@pytest.fixture
def url_year():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('year-list')


@pytest.fixture
def url_sector():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('sector-list')


@pytest.fixture
def url_program():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('program-list')


@pytest.fixture
def url_investment():
    """
    Fixture responsible for build the api url for main endpoint
    Returns Func:
    """
    return reverse('investment-list')


@pytest.mark.django_db
def test_years_list(client, url_year):
    """
    Testing list of years
    """
    # Create N objects
    request = client.get(path=url_year, format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list tags'
    assert len(request.data) == models.Year.objects.count(), 'Incorrect number objects in data'


@pytest.mark.django_db
def test_sectors_list(client, url_sector):
    """
    Testing list of sectors
    """
    # Create N objects
    request = client.get(path=url_sector, format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list tags'
    assert len(request.data) == models.Sector.objects.count(), 'Incorrect number objects in data'


@pytest.mark.django_db
def test_programs_list(client, url_program):
    """
    Testing list of programs
    """
    # Create N objects
    request = client.get(path=url_program, format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list tags'
    assert len(request.data) == models.Program.objects.count(), 'Incorrect number objects in data'


@pytest.mark.django_db
def test_investment_list(client, url_investment):
    """
    Testing list of investment
    """
    # Create N objects
    request = client.get(path=url_investment, format='json')

    assert request.status_code == status.HTTP_200_OK, 'Fails to list tags'
    assert len(request.data) == models.Investment.objects.count(), 'Incorrect number objects in data'
