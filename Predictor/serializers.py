from pyexpat import model
from attr import fields
from rest_framework import serializers
from . models import approvals

class approvalsSerializers(serializers.ModelSerializer):
    class Meta:
        model = approvals
        fields = '__all__'