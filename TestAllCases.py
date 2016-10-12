import unittest
from VideoToText import MainProcess
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    # def testRemoteVideo(self):
    #     try:
    #         main_process = MainProcess()
    #         self.assertTrue( main_process.initiateProcess(['remote_link=https://player.vimeo.com/external/180620123.sd.mp4?s=bce182385835eca58881a7cffbe71ecebb95f02a&profile_id=164&oauth2_token_id=2579535',
    #                                'type=video',
    #                                'text_file_path=faisal.txt',
    #                                'video_path=kashif.mp4']) )
    #     except:
    #         self.fail('Could not run testRemoteVideo properly')
    def testLocalVideo(self):
        try:
            main_process = MainProcess()
            self.assertTrue(main_process.initiateProcess(['local_path=/home/noaman/Documents/projects/ayeshaHelper/kashif.mp4',
                                                         'text_file_path=kashif.txt',
                                                         'type=video']))
        except:
            self.fail('Could not run testLocalAudio properly')
    if __name__ == '__main__':
        unittest.main()