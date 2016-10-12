import subprocess
from Settings import Settings
from copy import deepcopy

class Download:
    def __init__(self, local_file, download_url):
        command = str(deepcopy(Settings['Download Command']))
        command = command.replace('<vid_filename>', local_file).replace('<url>', download_url)
        subprocess.call(command.split())


