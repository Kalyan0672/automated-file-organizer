import unittest
import organizer


class TestFileOrganizer(unittest.TestCase):

    def test_image_file_category(self):
        self.assertIn(".jpg", organizer.FILE_CATEGORIES["Images"])

    def test_document_file_category(self):
        self.assertIn(".pdf", organizer.FILE_CATEGORIES["Documents"])

    def test_video_file_category(self):
        self.assertIn(".mp4", organizer.FILE_CATEGORIES["Videos"])

    def test_audio_file_category(self):
        self.assertIn(".mp3", organizer.FILE_CATEGORIES["Audio"])

    def test_presentation_file_category(self):
        self.assertIn(".pptx", organizer.FILE_CATEGORIES["Presentations"])


if __name__ == "__main__":
    unittest.main()