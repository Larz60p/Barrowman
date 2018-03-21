import BiblePaths
import CreateChapterJson
import ScrapeAudio
import UpdateBibleIndexAudioLinks


class RunMeOnce:
    def __init__(self):
        self.bpath = BiblePaths.BiblePaths()
        self.CCJ = CreateChapterJson.CreateChapterJson()
        self.CCJ.MakeBible()
        self.SA = ScrapeAudio.ScrapeAudio()
        self.SA.get_zip_files()
        self.UBIAL = UpdateBibleIndexAudioLinks.UpdateBibleIndexAudioLinks()


if __name__ == '__main__':
    RunMeOnce()
