from SpeechToTextBase import SpeechToTextBase
import speech_recognition as sr

class SphinxSpeechToText(SpeechToTextBase):
    def getText(self, audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
            try:
                return r.recognize_sphinx(audio)
            except sr.UnknownValueError:
                return 'Unknown Error'
            except sr.RequestError as e:
                return e.message
    def getSubtitles(self, audio_file):
        pass






