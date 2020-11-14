from rest_framework import serializers
from .models import Policy, Education, State


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ('category', 'title', 'sex', 'region',
                  'edu', 'age',  'state', 'benefits', 'desc')


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('edycation')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('stat')
