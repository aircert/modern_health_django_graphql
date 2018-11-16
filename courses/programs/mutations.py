import graphene
from .serializers import ProgramSerializer, WeekSerializer, PageSerializer
from graphene_django_extras import DjangoSerializerMutation


class ProgramSerializerMutation(DjangoSerializerMutation):
    """
        DjangoSerializerMutation auto implement Create, Delete and Update functions
    """
    class Meta:
        serializer_class = ProgramSerializer

class WeekSerializerMutation(DjangoSerializerMutation):
    """
        DjangoSerializerMutation auto implement Create, Delete and Update functions
    """
    class Meta:
        serializer_class = WeekSerializer

class PageSerializerMutation(DjangoSerializerMutation):
    """
        DjangoSerializerMutation auto implement Create, Delete and Update functions
    """
    class Meta:
        serializer_class = PageSerializer