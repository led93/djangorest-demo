from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from languages.models import Language
from languages.serializers import LanguageSerializer


class LanguageList(APIView):
    """
    List all languages, or create a new one
    """

    def get(self, request, format=None):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageDetail(APIView):
    """
    Retrieve, update or delete a language instance
    """

    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoseNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        language = self.get_object(pk=pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        language = self.get_object(pk=pk)
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        language = self.get_object(pk=pk)
        language.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
