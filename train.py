from src.cleaning import preprocessing
from src.api import get_transcript
from pipeline.model import model2
from pipeline.tts import tts

url = input("Enter youtube video link:  ")
id = preprocessing(url)
text = get_transcript(id)

# text = stt(file_path)
# t_summary = summary(text)
t_summary = model2(text)
tts(t_summary)