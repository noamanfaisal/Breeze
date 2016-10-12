# import subprocess
# import speech_recognition as sr
#sourcePath = "abc.mp4"
# targetPath = "audio.wav"
#vcommand = "ffmpeg -i " + sourcePath + " -ab 160k -ac 2 -ar 44100 -vn "+ targetPath
# subprocess.call(command, shell=True)
# with sr.AudioFile("audio.wav") as source:
import speech_recognition as sr
from os import path
import subprocess

def abc(fileName):
    rip(fileName)
    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), fileName+'.wav')
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source) # read the entire audio file
        try:
            file = open(fileName+'.txt', 'w')
            file.write(r.recognize_sphinx(audio))
            file.close()
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    print('Done')
def rip(fileName):
    command = 'ffmpeg -i '+'\''+fileName+'.mp4'+'\''+' -ab 160k -ac 2 -ar 44100 -vn '+'\''+fileName+'.wav\''
    subprocess.call(command, shell=True)

# ffmpeg -i test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav


abc(' Denver Introduction')
abc('20160924_120740')
abc('20160924_122052')
abc('20160924_130011')
abc('carnegieDeliClosing')
abc('FDA seeks input on new guidelines')
abc('Garavel Jeep Certified Pre-owned commercial- Sept 2016')
abc('Summer Fun With Mum_ Treasure Hunt')
abc('The StarsBest Kept Secrets_ Kate Winslet')
abc('USATodayEditorialBoard')

print("###########################################################################3")
print("Done Done Done Done Done Done Done Done Done Done Done")


