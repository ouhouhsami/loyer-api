"""loyerapi URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers, serializers, viewsets

from loyers.models import Loyer, AgglomerationDescription, Agglomeration, HousingType, ConstructionPeriod, RenterSeniority, NumberOfRooms


class LoyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Loyer
        fields = ('url', 'year', 'agglomeration', 'housing_type',
        		  'construction_period', 'renter_seniority', 'number_of_rooms',
        		  'agglomeration_description', 'loyer_median',
        		  'loyer_moyen', 'loyer_moyen')


class LoyerViewSet(viewsets.ModelViewSet):
    queryset = Loyer.objects.all()
    serializer_class = LoyerSerializer


class AgglomerationDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgglomerationDescription


class AgglomerationDescriptionViewSet(viewsets.ModelViewSet):
    queryset = AgglomerationDescription.objects.all()
    serializer_class = AgglomerationDescriptionSerializer


class AgglomerationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agglomeration

class AgglomerationViewSet(viewsets.ModelViewSet):
    queryset = Agglomeration.objects.all()
    serializer_class = AgglomerationSerializer


class HousingTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HousingType


class HousingTypeViewSet(viewsets.ModelViewSet):
    queryset = HousingType.objects.all()
    serializer_class = HousingTypeSerializer


class ConstructionPeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConstructionPeriod


class ConstructionPeriodViewSet(viewsets.ModelViewSet):
    queryset = ConstructionPeriod.objects.all()
    serializer_class = ConstructionPeriodSerializer


class RenterSenioritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RenterSeniority


class RenterSeniorityViewSet(viewsets.ModelViewSet):
    queryset = RenterSeniority.objects.all()
    serializer_class = RenterSenioritySerializer


class NumberOfRoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NumberOfRooms


class NumberOfRoomsViewSet(viewsets.ModelViewSet):
    queryset = NumberOfRooms.objects.all()
    serializer_class = NumberOfRoomsSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'loyers', LoyerViewSet)
router.register(r'agglomeration-description', AgglomerationDescriptionViewSet)
router.register(r'agglomeration', AgglomerationViewSet)
router.register(r'housing-type', HousingTypeViewSet)
router.register(r'construction-period', ConstructionPeriodViewSet)
router.register(r'renter-seniority', RenterSeniorityViewSet)
router.register(r'nb-of-rooms', NumberOfRoomsViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
