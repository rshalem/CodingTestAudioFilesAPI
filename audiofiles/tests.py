from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from audiofiles.models import AudioBook, Podcast, Song
from audiofiles.serializers import AudioBookSerializer, PodcastSerializer, SongSerializer

class AudioBookTest(APITestCase):
    def setUp(self):
        self.audiobook_instance = AudioBook.objects.create(audiobook_name='AudioBook 1',author='Ben',narrator='Shalem',duration_in_sec=300,uploaded_time=timezone.now())
        self.audio = AudioBook.objects.get(id=self.audiobook_instance.id)
        self.data = {'audiobook_name':'AudioBook New','author':'Jimmy','narrator':'Holi','duration_in_sec':300,'uploaded_time':timezone.now()}
        return super().setUp()

    def test_can_create_new_audiobook_instance(self):
        data = self.data
        response = self.client.post(reverse('audiofiles:create', kwargs={'audioFileType':'audiobook'}),data)
        self.assertEqual(response.status_code, 200)
    
    def test_can_read_single_audiobook(self):
        response = self.client.get(reverse('audiofiles:get-single', kwargs={'audioFileType':'audiobook', 'pk':self.audiobook_instance.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, AudioBookSerializer(instance=self.audiobook_instance).data)
        
    def test_can_update_audiobook(self):
        data = self.data
        response = self.client.put(reverse('audiofiles:update', kwargs={'audioFileType':'audiobook', 'pk':self.audio.id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_can_delete_audiobook(self):
        response = self.client.delete(reverse('audiofiles:delete', kwargs={'audioFileType':'audiobook', 'pk':self.audiobook_instance.id}))
        self.assertEqual(response.status_code, 200)
    
    def test_audio_serializer_works(self):
        data = self.data
        serialized = AudioBookSerializer(data=data)
        self.assertEqual(serialized.is_valid(), True)

class PodcastTest(APITestCase):
    def setUp(self):
        self.podcast_instance = Podcast(podcast_name='AudioBook 1',host='Ben',participants="['Naruto','James']",duration_in_sec=300,uploaded_time=timezone.now())
        self.podcast_instance.save(force_insert=True)
        self.audio = Podcast.objects.get(id=self.podcast_instance.id)
        self.data = {'podcast_name':'New','duration_in_sec':500,'uploaded_time':timezone.now(),'host':'Ben','participants':"['li','Chang']"}
        return super().setUp()

    def test_can_create_new_podcast_instance(self):
        data = self.data
        response = self.client.post(reverse('audiofiles:create', kwargs={'audioFileType':'podcast'}), data)
        self.assertEqual(response.status_code, 200)

    def test_can_read_podcast(self):
        self.podcast_instance = Podcast.objects.create(podcast_name='AudioBook 1',host='Ben',participants="['Naruto','James']",duration_in_sec=300,uploaded_time=timezone.now())
        response = self.client.get(reverse('audiofiles:get-single', kwargs={'audioFileType':'podcast', 'pk':self.podcast_instance.id}))
        self.assertEqual(response.status_code, 200)

    def test_can_update_podcast(self):
        data = self.data
        response = self.client.put(reverse('audiofiles:update', kwargs={'audioFileType':'podcast', 'pk':self.audio.id}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_podcast(self):
        response = self.client.delete(reverse('audiofiles:delete', kwargs={'audioFileType':'podcast', 'pk':self.podcast_instance.id}))
        self.assertEqual(response.status_code, 200)

    def test_participants_list_count(self):
        participant_count = len(self.podcast_instance.participants)
        self.assertEqual(participant_count, 2)
        
    def test_podcast_serializer_works(self):
        data = self.data
        serialized = PodcastSerializer(data=data)
        self.assertEqual(serialized.is_valid(), True)
    
    def test_podcast_serializer_doesnt_works(self):
        """incorrect data participants, passed as list without quotes"""
        incorrect_formatted_data = {'podcast_name':'New','duration_in_sec':500,'uploaded_time':timezone.now(),'host':'Ben','participants': ['li','Chang']}
        response = self.client.post(reverse('audiofiles:create', kwargs={'audioFileType':'podcast'}), incorrect_formatted_data)
        self.assertEqual(response.status_code, 400)

class SongTest(APITestCase):
    def setUp(self):
        self.song_instance = Song.objects.create(song_name='Baby',duration_in_sec=240,uploaded_time=timezone.now())
        self.song = Song.objects.get(id=self.song_instance.id)
        self.data = {'song_name':'Awesome','duration_in_sec':260, 'uploaded_time':timezone.now()}
        return super().setUp()

    def test_can_create_new_song_instance(self):
        data = self.data
        response = self.client.post(reverse('audiofiles:create', kwargs={'audioFileType':'song'}), data)
        self.assertEqual(response.status_code, 200)

    def test_can_read_song(self):
        response = self.client.get(reverse('audiofiles:get-single', kwargs={'audioFileType':'song', 'pk':self.song_instance.id}))
        self.assertEqual(response.status_code, 200)

    def test_can_update_song(self):
        data = self.data
        response = self.client.get(reverse('audiofiles:update', kwargs={'audioFileType':'song', 'pk':self.song_instance.id}),data=data)
        self.assertEqual(response.status_code, 200)

    def test_can_delete_song(self):
        response = self.client.delete(reverse('audiofiles:delete', kwargs={'audioFileType':'song', 'pk':self.song_instance.id}))
        self.assertEqual(response.status_code, 200)

    def test_song_serializer_works(self):
        data = self.data
        serialized = SongSerializer(data=data)
        self.assertEqual(serialized.is_valid(), True)
        self.assertEqual(serialized.data['song_name'], 'Awesome')