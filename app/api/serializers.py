from rest_framework import serializers
from app.models import Article, Recruiter, Employee, Apply

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = "__all__"

class RecruiterFlatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        exclude = ('id',)

class ArticleSerializer(serializers.ModelSerializer):
    #author = RecruiterSerializer(read_only=True)
    class Meta:
        model = Article
        fields = "__all__"
    def to_representation(self, instance):
        self.fields['author']=RecruiterSerializer(read_only=True)
        return super(ArticleSerializer, self).to_representation(instance)

class ArticleSimpleSerializer(serializers.ModelSerializer):
    author = RecruiterFlatterSerializer(read_only=True)

    class Meta:
        model = Article
        exclude= ('description',)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        article_representation = representation.pop('author')
        for key in article_representation:
            representation[key] = article_representation[key]
        return representation

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

class ApplySerializer(serializers.ModelSerializer):
    
    class Meta:
        verbose_name_plural='applies'
        model = Apply
        exclude = ('id',)