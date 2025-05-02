from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import locale
import soundfile as sf


pipeline = KPipeline(lang_code='a')

def tts(summary):
  generator = pipeline(summary, voice= 'af_heart', speed=1) # Use pipeline instead of k_pipeline, as pipeline is the KPipeline object you instantiated
  for i, (gs, ps, audio) in enumerate(generator):
    output_path = f"output_audio_{i}.wav"
    sf.write(output_path, audio, 24000)
    print(f"[✔] Audio saved at: {output_path}")

def getpreferredencoding(do_setlocale = True):
    return "UTF-8"
locale.getpreferredencoding = getpreferredencoding

