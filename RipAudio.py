# # import subprocess
# # import speech_recognition as sr
# #sourcePath = "abc.mp4"
# # targetPath = "audio.wav"
# #vcommand = "ffmpeg -i " + sourcePath + " -ab 160k -ac 2 -ar 44100 -vn "+ targetPath
# # subprocess.call(command, shell=True)
# # with sr.AudioFile("audio.wav") as source:
# import speech_recognition as sr
# from os import path
# import subprocess
#
# def abc(fileName):
#     rip(fileName)
#     AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), fileName+'.wav')
#     r = sr.Recognizer()
#     with sr.AudioFile(AUDIO_FILE) as source:
#         audio = r.record(source) # read the entire audio file
#         try:
#             file = open(fileName+'.txt', 'w')
#             file.write(r.recognize_sphinx(audio))
#             file.close()
#         except sr.UnknownValueError:
#             print("Sphinx could not understand audio")
#         except sr.RequestError as e:
#             print("Sphinx error; {0}".format(e))
#     print('Done')
# def rip(fileName):
#     command = 'ffmpeg -i '+fileName+'.mp4'+' -ab 160k -ac 2 -ar 44100 -vn '+fileName+'.wav'
#     subprocess.call(command, shell=True)
#
# # ffmpeg -i test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav
# abc('A_Social_Media_Outcry_Saved_Karma_The_Wolf_Dog_From_Euthanasia')
# abc('Israeli_Team_Books_Their_Ticket_To_The_Moon')
# abc('NoNote7NYC')
# abc('Washington_Redskins_Defensive_Rookies_Pick_Up')
#
#
#
import subprocess
from Settings import Settings
from copy import deepcopy
class RipAudio:
    def __init__(self, video_file, audio_file):
        command = str(deepcopy(Settings['FFMPEG Command']))
        command = command.replace('<vid_filename>', video_file).replace('<aud_filename>', audio_file)
        subprocess.call(command.split())