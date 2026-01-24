# содержит представления для обработки запросов апи 
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Note
from .serializers import NoteCreateSerializer, NoteSerializer, NoteUpdateSerializer


class NoteListCreateViews(generics.ListAPIView):
    queryset = None.objects.all()

    def get_serializer_class(self):
 
        return NoteSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        if self.request.method == ["POST", "PATCH"]:
            return NoteCreateSerializer
        return NoteSerializer
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', false)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            self.perform_update(serializer)
