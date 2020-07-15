from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addincome/', views.addincome, name='add-income'),
    path('listincome/', views.AllIncome, name='list-income'),
    path('deleteincome/<int:id>/', views.Deleteincome, name='delete-income'),
    path('<int:id>/', views.addincome, name='update-income'),
    path('listexpenses/', views.AllExpenses, name='list-expenses'),
    path('<int:id>/', views.addexpenses, name='update-expenses'),
    path('addexpenses/', views.addexpenses, name='add-expenses'),
    path('deleteexpenses/<int:id>/', views.Deleteexpenses, name='delete-expenses'),
    path('setbudget/', views.SetBudget, name='set-budget'),
    path('search/', views.search, name='search'),
]
