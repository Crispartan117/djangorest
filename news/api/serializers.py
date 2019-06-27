from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        exclude = ("id",)
        #fields = "__all__" # Agregamos todos los campos del modelo
        #fields = ("title", "description", "body") # Agregamos solo los campos seleccionados.
    
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

""" class ArticleSerializer(serializers.Serializer):
    id                  = serializers.IntegerField(read_only=True)
    author              = serializers.CharField()
    title               = serializers.CharField()
    description         = serializers.CharField()
    body                = serializers.CharField()
    location            = serializers.CharField()
    publication_date    = serializers.DateField()
    active              = serializers.BooleanField()
    created_at          = serializers.DateTimeField(read_only=True)
    updated_at          = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data): #No se actualiza la informacion de solo lectura.
        instance.author             = validated_data.get('author', instance.author)
        instance.title              = validated_data.get('title', instance.title)
        instance.description        = validated_data.get('description', instance.description)
        instance.body               = validated_data.get('body', instance.body)
        instance.location           = validated_data.get('location', instance.location)
        instance.publication_date   = validated_data.get('publication_date', instance.publication_date)
        instance.active             = validated_data.get('active', instance.active)
        instance.save()
        return instance

    #Comparativo.
    def validate(self, data):
        if data["title"] == data["description"]: #Compara si las cadenas de datos de titulo y descripcion son diferentes.
            raise serializers.ValidationError("Title and Description must be different!")
        return data
    
    #Por campo.
    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError("The title must be at least 60 characters!")
        return value """
    
    
        





