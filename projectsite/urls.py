"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cardquest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerListView.as_view(), name='trainer-list'),
    path('collection_list', views.CollectionListView.as_view(), name='collection-list'),
    path('pokemon_card', views.PokemonCardListView.as_view(), name='pokemon-card'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'),
    path('pokemoncard_list', views.PokemonCardListView.as_view(), name='pokemoncard-list'),
    path('collection_list/add', views.CollectionCreateView.as_view(), name='collection-add'),
    path('collection_list/<pk>', views.CollectionUpdateView.as_view(), name='collection-update'),
    path('collection_list/<pk>/delete', views.CollectionDeleteView.as_view(), name='collection-delete'),
    ]
