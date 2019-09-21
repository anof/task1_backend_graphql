import graphene
from graphene_django.types import DjangoObjectType
from .models import Music

class MusicType(DjangoObjectType):
    class Meta:
        model = Music

class Query(graphene.ObjectType):
    all_music = graphene.List(MusicType)

    def resolve_all_music(self, info):
        return  Music.objects.all()
