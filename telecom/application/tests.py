import pytest
from django.urls import reverse
from .models import Customer

@pytest.mark.django_db
def test_customer_list_view(client):
    response = client.get(reverse('customer_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_customer_detail_view(client):
    customer = Customer.objects.create(name='Test Customer', email='test@example.com')
    response = client.get(reverse('customer_detail', kwargs={'pk': customer.pk}))
    assert response.status_code == 200

@pytest.mark.django_db
def test_customer_create_view(client):
    response = client.post(reverse('add_customer'), {'name': 'New Customer', 'email': 'new@example.com'})
    assert response.status_code == 302  # Redirects after successful creation

@pytest.mark.django_db
def test_renew_plan_view(client):
    customer = Customer.objects.create(name='Test Customer', email='test@example.com')
    response = client.post(reverse('renew_plan', kwargs={'pk': customer.pk}), {'name': 'Test Customer', 'email': 'test@example.com'})
    assert response.status_code == 302  # Redirects after successful plan renewal

@pytest.mark.django_db
def test_customer_create_view_with_invalid_data(client):
    response = client.post(reverse('add_customer'), {})  # Sending empty data intentionally
    assert response.status_code == 200  # Should return to the same page with validation errors

@pytest.mark.django_db
def test_renew_plan_view_with_invalid_data(client):
    customer = Customer.objects.create(name='Test Customer', email='test@example.com')
    response = client.post(reverse('renew_plan', kwargs={'pk': customer.pk}), {})  # Sending empty data intentionally
    assert response.status_code == 200  # Should return to the same page with validation errors
