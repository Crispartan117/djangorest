from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers
from news.models import Article, Journalist

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        exclude = ("id",)
        #fields = "__all__" # Agregamos todos los campos del modelo
        #fields = ("title", "description", "body") # Agregamos solo los campos seleccionados.

        time_since_publication = serializers.SerializerMethodField()
        #author = JournalistSerializer(read_only=True) 
        #author = serializers.StringRelatedField()
    
    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta


    #Comparativo.
    def validate(self, data):
        if data["title"] == data["description"]: #Compara si las cadenas de datos de titulo y descripcion son diferentes.
            raise serializers.ValidationError("Title and Description must be different!")
        return data
    
    #Por campo.
    def validate_title(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("The title must be at least 30 characters!")
        return value

class JournalistSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                read_only=True,
                                                view_name="article-detail")
    #articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist
        fields = "__all__"
    

    

        





