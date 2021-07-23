from .models import assignTaskFiles, userprofile , Objectcategories
from rest_framework import serializers
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = '__all__'

class ObjectcategoriesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Objectcategories
        fields = ('id',
                  'object_category')
class assignTaskFilesserializer(serializers.ModelSerializer):
     class Meta:
        model = assignTaskFiles
        fields = (
                  'File_Name','project_name','Task_level','Priority','Created_Date','status','Action','annotation_image')