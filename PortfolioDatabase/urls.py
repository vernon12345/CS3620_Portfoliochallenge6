from . import views
from django.contrib import admin
from django.urls import path
app_name = 'PortfolioDatabase'

urlpatterns = [#url patterns
    path('<int:portfolio_id>', views.detail2, name='detail2'),
    path('<int:Hobby_id>', views.detail, name='detail'),  # url paths
    path('Home/', views.Home, name='Home'),#url paths
    path('index/', views.index, name='index'),  # url paths
    path('Hobbies/', views.Hobbies, name='Hobbies'),#url paths
    path('Portfolio/', views.Portfolio, name='Portfolio'),#url paths
    path('Contact/', views.Contact, name='Contact'),#url paths
    path('Add/', views.create_hobby, name='create_hobby'),#url paths
    path('Addcontact/', views.create_contact, name='create_contact'),  # url paths
    path('Update/<int:id>', views.update_portfolio, name='update_portfolio'),#url paths
    path('Delete/<int:id>', views.delete_portfolio, name='delete_Portfolio'),#url paths
]
