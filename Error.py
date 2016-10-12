error_dict = {
                'PATH_ERROR':' path not available or permission denied',
                'FILE_DOES_NOT_EXIST':' file not exist or permission denied',
                'DOWNLOAD_FAIL':' could not download, please check your internet and try again',
                'REMOTE_LINK_EMPTY':'remote link empty or not available',
                'TYPE_NOT_MENTIONED':' type wrongly mentioned only video or audio is allowed',
                'TYPE_WRONGLY_MENTIONED':' type wrongly mentioned only video or audio is allowed',
                'VIDEO_PATH_NOT_GIVEN':'video path is not given',
                'TEXT_PATH_NOT_GIVEN':'text path is not given',
                'AUDIO_PATH_NOT_GIVEN':'audio path is not given',
                'LOCAL_PATH_NOT_GIVEN':'local path is not given',
                'VIDEO_FILE_NOT_GIVEN':'Video file is not given',
                'AUDIO_FILE_NOT_GIVEN': 'Video file is not given',
                'TEXT_FILE_NOT_GIVEN': 'Video file is not given',
                'VIDEO_EXTENSION_NOT_GIVEN': 'Video file extension is not given',
                'AUDIO_EXTENSION_NOT_GIVEN': 'Audio file extension is not given',
                'COULD_NOT_CREATE_AUDIO': 'Could not create audio',
                'COULD_NOT_CREATE_TEXT': 'Could not create text',

}
print_message = {
                    'CHANGING_PATH_TO_CURRENT_DIRECTORY':'Changing path to current directory',
}
class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message

class PathNotExist(Error):
    def __init__(self, path):
        super(PathNotExist,  self).__init__(path + error_dict['PATH_ERROR'])

class FileNotExist(Error):
    def __init__(self, file_name_with_path):
        super(FileNotExist,  self).__init__(file_name_with_path + error_dict['FILE_DOES_NOT_EXIST'])

class CouldNotDownload(Error):
    def __init__(self, file_name_with_path):
        super(PathNotExist,  self).__init__(file_name_with_path + error_dict['DOWNLOAD_FAIL'])

class RemoteLinkEmpty(Error):
    def __init__(self):
        super(RemoteLinkEmpty,  self).__init__(error_dict['REMOTE_LINK_EMPTY'])

class TypeNotMentioned(Error):
    def __init__(self):
        super(TypeNotMentioned,  self).__init__(error_dict['TYPE_NOT_MENTIONED'])

class TypeWronglyMentioned(Error):
    def __init__(self, type_mentioned):
        super(TypeWronglyMentioned,  self).__init__(error_dict['TYPE_WRONGLY_MENTIONED'])

class VideoPathNotGiven(Error):
    def __init__(self):
        super(VideoPathNotGiven, self).__init__(error_dict['VIDEO_PATH_NOT_GIVEN'])

class TextPathNotGiven(Error):
    def __init__(self):
        super(TextPathNotGiven, self).__init__(error_dict['TEXT_PATH_NOT_GIVEN'])

class AudioPathNotGiven(Error):
    def __init__(self):
        super(TextPathNotGiven, self).__init__(error_dict['AUDIO_PATH_NOT_GIVEN'])

class LocalPathEmpty(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['LOCAL_PATH_NOT_GIVEN'])

class VideoFileNotGiven(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['VIDEO_FILE_NOT_GIVEN'])

class AudioFileNotGiven(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['AUDIO_FILE_NOT_GIVEN'])

class TextFileNotGiven(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['TEXT_FILE_NOT_GIVEN'])

class VideoExtenstionNotGiven(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['VIDEO_EXTENSION_NOT_GIVEN'])

class AudioExtenstionNotGiven(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['AUDIO_EXTENSION_NOT_GIVEN'])

class CouldNotCreateAudio(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['COULD_NOT_CREATE_AUDIO'])

class CouldNotCreateText(Error):
    def __init__(self):
        super(LocalPathEmpty,  self).__init__(error_dict['COULD_NOT_CREATE_TEXT'])