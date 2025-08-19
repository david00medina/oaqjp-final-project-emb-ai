import unittest

from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    JOY = "I am glad this happened"
    ANGER = "I am really mad about this"
    DISGUST = "I feel disgusted just hearing about this"
    SADNESS = "I am so sad about this"
    FEAR = "I am really afraid that this will happen"
    def test_joy(self):
        dominant_emotion = emotion_detector(self.JOY).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "joy")

    def test_anger(self):
        dominant_emotion = emotion_detector(self.ANGER).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "anger")

    def test_disgust(self):
        dominant_emotion = emotion_detector(self.DISGUST).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "disgust")
    
    def test_sadness(self):
        dominant_emotion = emotion_detector(self.SADNESS).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "sadness")

    def test_fear(self):
        dominant_emotion = emotion_detector(self.FEAR).get("dominant_emotion")
        self.assertEqual(dominant_emotion, "fear")