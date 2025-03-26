from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import locale


pipeline = KPipeline(lang_code='a')

def tts(summary):
  generator = pipeline(summary, voice= 'af_heart', speed=1) # Use pipeline instead of k_pipeline, as pipeline is the KPipeline object you instantiated
  for i, (gs, ps, audio) in enumerate(generator):
    display(Audio(data=audio, rate=24000, autoplay=True))


def getpreferredencoding(do_setlocale = True):
    return "UTF-8"
locale.getpreferredencoding = getpreferredencoding

