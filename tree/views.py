from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Person, Relationship
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person, Relationship
from .serializers import PersonSerializer, RelationshipSerializer

@api_view(['GET'])
def family_tree_api(request):
    persons = Person.objects.all()
    relationships = Relationship.objects.all()
    person_serializer = PersonSerializer(persons, many=True)
    relationship_serializer = RelationshipSerializer(relationships, many=True)
    return Response({
        'persons': person_serializer.data,
        'relationships': relationship_serializer.data
    })


def family_tree(request):
    persons = Person.objects.all()
    relationships = Relationship.objects.all()
    context = {
        'persons': persons,
        'relationships': relationships,
    }
    return render(request, 'tree/family_tree.html', context)
