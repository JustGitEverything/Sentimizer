from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DiaryEntry
from .serializers import DiaryEntrySerializer


# Create your views here.
@api_view(["GET", "POST"])
def diary_entry(request):
    if request.method == "GET":
        entries = DiaryEntry.objects.all()
        serializer = DiaryEntrySerializer(entries, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DiaryEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
