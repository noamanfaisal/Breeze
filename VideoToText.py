#!/usr/bin/env python
import sys
from Settings import SettingsLoader
from Settings import Settings
from RipAudio import RipAudio
from Download import Download
import os
from SpeechToTextFactory import SpeechToTextFactory
from SphinxSpeechToText import SphinxSpeechToText
from RipAudio import RipAudio
from Error import PathNotExist
from Error import FileNotExist
from Error import CouldNotDownload
from Error import RemoteLinkEmpty
from Error import TypeNotMentioned
from Error import TypeWronglyMentioned
from Error import VideoPathNotGiven
from Error import TextPathNotGiven
from Error import AudioPathNotGiven
from Error import LocalPathEmpty
from Error import print_message
from Error import VideoExtenstionNotGiven
from Error import AudioExtenstionNotGiven
from Error import VideoFileNotGiven
from Error import AudioFileNotGiven
from Error import CouldNotCreateAudio
from Error import CouldNotCreateText



# dictionary

# load settings
##############################################

##############################################
class MainProcess:

    def __init__(self):
        # process if its for settings
        # process if its download audio
        # process if its download video
        # process if its local audio
        # process if its local video
        # dictionary of exit
        pass

    def initiateProcess(self, command_parameters):
        if len(command_parameters) == 1:
            # do something for settings
            if command_parameters == 'settings'.lower():
                self.settings()
        elif len(command_parameters) == 4:
            # find text file path
            if any('text_file_path' in s.lower() for s in command_parameters):
                text_file_path_expression = [s for s in command_parameters if 'text_file_path' in s.lower()]
                text_file_path = text_file_path_expression[0].split('=')[1].strip()
            else:
                raise TextPathNotGiven()
            if any('remote_link' in s.lower() for s in command_parameters):
                remote_link_expression = [s for s in command_parameters if 'remote_link' in s.lower()]
                # an argument has been passed, because only first occurrance of = will be catch and rest in link these will be ignored
                remote_link = remote_link_expression[0].split('=', 1)[1].strip()
                if remote_link == '':
                    raise RemoteLinkEmpty()
                else:
                    if any('type' in s.lower() for s in command_parameters):
                        type_expression = [s for s in command_parameters if 'type' in s.lower()]
                        type_name = type_expression[0].split('=')[1].strip()
                        if type_name == '':
                            raise TypeNotMentioned()
                        elif str(type_name).lower() == 'video':
                            if any('video_path' in s.lower() for s in command_parameters):
                                video_path_expression = [s for s in command_parameters if 'video_path' in s.lower()]
                                video_path = video_path_expression[0].split('=')[1].strip()
                                if video_path == '':
                                    raise VideoPathNotGiven()
                                else:
                                    self.remoteVideo(remote_link, video_path, text_file_path)
                            else:
                                raise VideoPathNotGiven()
                        elif str(type_name).lower() == 'audio':
                            if any('audio_path' in s.lower() for s in command_parameters):
                                audio_path_expression = [s for s in command_parameters if 'audio_path' in s.lower()]
                                audio_path = audio_path_expression.split('=')[1].strip()
                                if audio_path == '':
                                    raise AudioPathNotGiven()
                                else:
                                    self.remoteAudio(remote_link, audio_path, text_file_path)
                            else:
                                raise VideoPathNotGiven()
                        else:
                            raise TypeWronglyMentioned(type_name)
            else:
                raise VideoPathNotGiven()
            return True

        elif len(command_parameters) == 3:
            # find text file path
            if any('text_file_path' in s.lower() for s in command_parameters):
                text_file_path_expression = [s for s in command_parameters if 'text_file_path' in s.lower()]
                text_file_path = text_file_path_expression[0].split('=')[1].strip()
            else:
                raise TextPathNotGiven()
            if any('local_path' in s.lower() for s in command_parameters):
                local_path_expression = [s for s in command_parameters if 'local_path' in s.lower()]
                local_path = local_path_expression[0].split('=')[1].strip()
                if local_path == '':
                    raise LocalPathEmpty()
                else:
                    if any('type' in s.lower() for s in command_parameters):
                        type_expression = [s for s in command_parameters if 'type' in s.lower()]
                        type_name = type_expression[0].split('=')[1].strip()
                        if type_name == '':
                            raise TypeNotMentioned()
                        elif str(type_name).lower() == 'video':
                            # if any('video_path' in s.lower() for s in command_parameters):
                            #     video_path_expression = [s for s in command_parameters if 'video_path' in s.lower()]
                            #     video_path = video_path_expression[0].split('=')[1].strip()
                            #     if video_path == '':
                            #         raise VideoPathNotGiven()
                            #     else:
                            #         self.localVideo(video_path, text_file_path)
                            # else:
                            #     raise VideoPathNotGiven()
                            self.localVideo(local_path, text_file_path)
                        elif str(type_name).lower() == 'audio':
                            if any('audio_path' in s.lower() for s in command_parameters):
                                audio_path_expression = [s for s in command_parameters if 'audio_path' in s.lower()]
                                audio_path = audio_path_expression[0].split('=')[1].strip()
                                if audio_path == '':
                                    raise AudioPathNotGiven()
                                else:
                                    self.localAudio(audio_path, text_file_path)
                            else:
                                raise AudioPathNotGiven()
                        else:
                            raise TypeWronglyMentioned(type_name)
            return True
        else:
            return False

    def settings(self):
        pass

    def ifFileExists(self, file_name_with_path):
        if os.path.isfile(file_name_with_path):
            return True
        else:
            raise FileNotExist(file_name_with_path)

    def getPathAndFileNameAndExtension(self, file_name_with_path):
        path, file_name = os.path.split(file_name_with_path)
        file_name_with_path_without_extension, extension = os.path.splitext(file_name_with_path)
        return path, file_name, file_name_with_path_without_extension, extension

    def renameOrDeleteFileNameAndConfirmPath(self, file_name_with_path, rename_or_delete, excetpion_type):
        path, file_name, file_name_without_extension_with_path, extension = self.getPathAndFileNameAndExtension(file_name_with_path)
        if path == '':
            # adding current path
            print print_message['CHANGING_PATH_TO_CURRENT_DIRECTORY']
            path = os.getcwd()
            file_name_without_extension_with_path = os.path.join(path, file_name_without_extension_with_path)
            file_name_with_path = os.path.join(path, file_name_with_path)
        if extension == '':
            if excetpion_type == 'audio':
                raise AudioExtenstionNotGiven
            elif excetpion_type == 'video':
                raise VideoExtenstionNotGiven
        if file_name == '':
            if excetpion_type == 'audio':
                raise AudioFileNotGiven
            elif excetpion_type == 'video':
                raise VideoFileNotGiven
        # confirm path
        if not os.path.isdir(path):
            raise PathNotExist(path)
        # rename or delete if file exists
        if rename_or_delete == True: # means if yes it is to be rename otherwise it is to be delete
            return self.renameIfFileExists(file_name_with_path)
        else:
            if os.path.isfile(file_name_with_path):
                os.remove(file_name_with_path)
                return file_name_with_path
        return file_name_with_path

    def renameIfFileExists(self, file_name_with_path):
        file_name_with_path_without_extension, extension = os.path.splitext(file_name_with_path)
        counter = 0
        while (True):
            if os.path.isfile(file_name_with_path) == False:
                break
            file_name_with_path = file_name_with_path_without_extension+'_'+str(counter)+extension
            counter = counter + 1
        return file_name_with_path



    def remoteAudio(self, download_link, audio_link, text_file_and_path):
        audio_link = self.renameOrDeleteFileNameAndConfirmPath(audio_link, True, 'audio')
        # download file
        Download(audio_link, download_link)
        # confirm audio_file
        if os.path.isfile(audio_link):
            raise CouldNotDownload
        # get text of voice
        text_file_and_path = self.renameOrDeleteFileNameAndConfirmPath(text_file_and_path, False, 'text')
        self.getTextFromAudio(audio_link, text_file_and_path)

    def localAudio(self, audio_link, text_file_and_path):
        self.ifFileExists(audio_link)
        text_file_and_path = self.renameOrDeleteFileNameAndConfirmPath(text_file_and_path, False, 'text')
        self.getTextFromAudio(audio_link, text_file_and_path)

    def remoteVideo(self, download_link, video_link, text_file_and_path):
        video_link = self.renameOrDeleteFileNameAndConfirmPath(video_link, True, 'video')
        # download file
        Download(video_link, download_link)
        # delete if audio_file available
        file_name_without_extension = os.path.splitext(video_link)[0]
        # audio_link = selfrenameOrDeleteFileNameAndConfirmPath(file_name_without_extension + Settings['Audio File Extension'],
        #                                              False)
        audio_link = self.renameOrDeleteFileNameAndConfirmPath(file_name_without_extension + Settings['Audio File Extension'], False, 'audio')
        RipAudio(video_link, audio_link)
        if not os.path.isfile(audio_link):
            raise CouldNotCreateAudio
        text_file_and_path = self.renameOrDeleteFileNameAndConfirmPath(text_file_and_path, False, 'text')
        self.getTextFromAudio(audio_link, text_file_and_path)
        if not os.path.isfile(text_file_and_path):
            raise CouldNotCreateText

    def localVideo(self, video_link, text_file_and_path):
        self.ifFileExists(video_link)
        file_name_without_extension = os.path.splitext(video_link)[0]
        audio_link = self.renameOrDeleteFileNameAndConfirmPath(
                                                        file_name_without_extension + Settings['Audio File Extension'],
                                                        False, 'audio')
        RipAudio(video_link, audio_link)
        if not os.path.isfile(audio_link):
            raise CouldNotCreateAudio
        text_file_and_path = self.renameOrDeleteFileNameAndConfirmPath(text_file_and_path, False, 'text')
        self.getTextFromAudio(audio_link, text_file_and_path)
        if not os.path.isfile(text_file_and_path):
            raise CouldNotCreateText

    def getTextFromAudio(self, audio_link, text_file_path):
        if Settings['Use Sphinx'] == 'Yes':
            sphinx_method_from_audio_to_text = SpeechToTextFactory().create('sphinx')
            with open(text_file_path, 'w+') as text_file:
                text_file.write(sphinx_method_from_audio_to_text.getText(audio_link))

# main
if __name__ == "__main__":
    print os.getcwd()
    settings = SettingsLoader()
    main_process = MainProcess()
    command_parameters = sys.argv[1:]
    main_process.initiateProcess(command_parameters)
    print "Thanks for using Breeze Auto Subtitler program"
    print "Developed & Designed by Noaman Faisal Bin Badar"











