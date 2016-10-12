import pickle
import os
import configparser
from configparser import ConfigParser
Settings = dict()
class SettingsLoader:

    def __init__(self):
        self.ConfigFile = 'videoToTextSettings.conf'
        self.load()

    def load(self):
        config = ConfigParser()
        self.home_directory = os.getcwd()

        self.software_home_directory = os.path.join(self.home_directory, 'conf')
        if not os.path.isdir(self.software_home_directory):
            os.mkdir(self.software_home_directory)
        self.software_config_file = os.path.join(self.software_home_directory, self.ConfigFile)
        if not os.path.isfile(self.software_config_file):
            #config.add_section('Default')
            config.add_section('Ripping')
            config.add_section('Download')
            config.add_section('Speech To Text')
            #config.set('Default', 'Temp Folder', os.path.join(self.software_home_directory,'temp'))
            #os.mkdir(os.path.join(self.software_home_directory,'temp'))
            config.set('Ripping', 'FFMPEG Command', 'ffmpeg -i <vid_filename> -ab 160k -ac 2 -ar 44100 -vn <aud_filename>')
            config.set('Ripping', 'Audio File Extension', '.wav')

            config.set('Download', 'Download Command', 'wget <url> -O <vid_filename> -c')
            config.set('Speech To Text', 'Use Sphinx', 'Yes')

            Settings['FFMPEG Command'] = 'ffmpeg -i <vid_filename> -ab 160k -ac 2 -ar 44100 -vn <aud_filename>.wav'
            Settings['Download Command'] = 'wget <url> -O <vid_filename> -c'
            Settings['Audio File Extension'] = '.wav'
            Settings['Use Sphinx'] = 'Yes'
            # Writing our configuration file to 'example.cfg'
            with open(self.software_config_file, 'wb') as configfile:
                config.write(configfile)
        else:
            config.read(self.software_config_file)
            Settings['FFMPEG Command'] = config.get('Ripping', 'FFMPEG Command')
            Settings['Download Command'] = config.get('Download', 'Download Command')
            Settings['Use Sphinx'] = config.get('Speech To Text', 'Use Sphinx')
            Settings['Audio File Extension'] = config.get('Ripping', 'Audio File Extension')
            #  = config['Default']['Temp Folder']
            # Settings['FFMPEG Command'] = config['Ripping']['FFMPEG Command']
            #
            #