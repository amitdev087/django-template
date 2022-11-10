from rest_framework import serializers

from .models import Students


class StudentsSerializers(serializers.ModelSerializer):
    firstName=serializers.CharField(max_length=100,required=True)
    lastName=serializers.CharField(max_length=100,required=True)
    address=serializers.CharField(max_length=100,required=True)
    rollNumber=serializers.IntegerField()
    phone=serializers.CharField(max_length=100,required=True)


    class Meta:
        model=Students
        fields=("__all__")
