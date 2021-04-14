from functools import partial
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from audiofiles.models import AudioBook, Podcast, Song
from audiofiles.serializers import AudioBookSerializer, PodcastSerializer, SongSerializer

class AudioFileCreateAndReadView(APIView):
    """CBV to handle Request and provide required response, here creating and reading audiofiles"""

    def get(self, request, format=None, *args, **kwargs):
        """getting all audiofile objects"""
        audio_file = kwargs.get('audioFileType','')
        audio_file_type = audio_file.lower()

        if audio_file_type == 'audiobook':
            obj = AudioBook.objects.all()
            serializer = AudioBookSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if audio_file_type == 'podcast':
            obj = Podcast.objects.all()
            serializer = PodcastSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if audio_file_type == 'song':
            obj = Song.objects.all()
            serializer = SongSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None, *args, **kwargs):
        """creating new audiofile instances"""
        try:
            data = request.data
            audio_file = kwargs.get('audioFileType','')
            audio_file_type = audio_file.lower()

            if audio_file_type == 'audiobook':
                serializer = AudioBookSerializer(data=data)
                if serializer.is_valid():

                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if audio_file_type == 'podcast':
                serializer = PodcastSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if audio_file_type == 'song':
                serializer = SongSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AudioFileReadDetailUpdateDelete(APIView):
    """CBV to handle Request and provide required response, here getting,updating or deleting audiofiles"""

    def get(self, request, pk, format=None, *args, **kwargs):
        """getting a single instance of audiofile using primarykey"""
        try:
            audio_file = kwargs.get('audioFileType','')
            audio_file_type = audio_file.lower()

            if audio_file_type == 'audiobook':
                obj = get_object_or_404(AudioBook, id=pk)
                serializer = AudioBookSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)

            if audio_file_type == 'podcast':
                obj = get_object_or_404(Podcast, id=pk)
                serializer = PodcastSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)

            if audio_file_type == 'song':
                obj = get_object_or_404(Song, id=pk)
                serializer = SongSerializer(obj)
                return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None, *args, **kwargs):
        """updating a single instance of audiofile using primarykey"""
        try:
            data = request.data
            audio_file = kwargs.get('audioFileType','')
            audio_file_type = audio_file.lower()
            
            if audio_file_type == 'audiobook':
                audio_instance = get_object_or_404(AudioBook, id=pk)
                serializer = AudioBookSerializer(audio_instance, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if audio_file_type == 'podcast':
                audio_instance = get_object_or_404(Podcast, id=pk)
                
                serializer = PodcastSerializer(audio_instance, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if audio_file_type == 'song':
                audio_instance = get_object_or_404(Song, id=pk)
                serializer = SongSerializer(audio_instance, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk, format=None, *args, **kwargs):
        """deleting an instance of audiofile using primarykey"""
        try:
            audio_file = kwargs.get('audioFileType','')
            audio_file_type = audio_file.lower()
            
            if audio_file_type == 'audiobook':
                audio_instance = get_object_or_404(AudioBook, id=pk)
                audio_instance.delete()
                return Response(status=status.HTTP_200_OK)

            if audio_file_type == 'podcast':
                audio_instance = get_object_or_404(Podcast, id=pk)
                audio_instance.delete()
                return Response(status=status.HTTP_200_OK)

            if audio_file_type == 'song':
                audio_instance = get_object_or_404(Song, id=pk)
                audio_instance.delete()
                return Response(status=status.HTTP_200_OK)
            
        except Exception:
            error = {'error':'Please provide correct audiofile ID'}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
