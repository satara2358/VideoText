import whisper
import pytube

youtubeId = 'https://www.youtube.com/watch?v=JtcpAmOUshM&list=RDJtcpAmOUshM&start_radio=1'
model = whisper.load_model('small')
youtube = pytube.YouTube(youtubeId)
audio = youtube.streams.get_audio_only()
audio.download(filename='audio.mp4')
result = model.transcribe('audio,mp4')

print(result["text"])