from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User

from .models import Consulting, Answer
from .serializers import ConsultingSerializer, AnswerSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def consulting_list(request):
    if request.method == 'GET':
        consultings = Consulting.objects.all()
        serializer = ConsultingSerializer(consultings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ConsultingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            consulting = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def consulting_detail(request, consulting_pk):
    consulting = Consulting.objects.get(pk=consulting_pk)

    if request.method == 'GET':
        serializer = ConsultingSerializer(consulting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        consulting.delete()
        return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ConsultingSerializer(consulting, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def answer_create(request, consulting_pk):
    consulting = Consulting.objects.get(pk=consulting_pk)
    serializer = AnswerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(consulting=consulting, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)