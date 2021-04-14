from rest_framework.serializers import ModelSerializer

from audiofiles.models import AudioBook, Podcast, Song

class AudioBookSerializer(ModelSerializer):
    """serializes and deserializes instances of AudioBook"""
    class Meta:
        model = AudioBook
        fields = ['id', 'audiobook_name', 'author','narrator','duration_in_sec','uploaded_time']

class PodcastSerializer(ModelSerializer):
    """serializes and deserializes instances of Podcast"""
    
    class Meta:
        model = Podcast
        fields = ['id', 'podcast_name', 'duration_in_sec','uploaded_time','host','participants']

class SongSerializer(ModelSerializer):
    """serializes and deserializes instances of Song"""
    class Meta:
        model = Song
        fields = ['id', 'song_name', 'duration_in_sec', 'uploaded_time']