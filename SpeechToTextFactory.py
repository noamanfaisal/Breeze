from SphinxSpeechToText import SphinxSpeechToText
class SpeechToTextFactory:
    def create(self, decision):
        if decision == 'sphinx':
            return SphinxSpeechToText()
        else:
            pass