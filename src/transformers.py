import torch
from transformers import pipeline


whisper = pipeline("automatic-speech-recognition", "openai/whisper-large-v3", torch_dtype=torch.float16, device="cuda:0")

def stt(file_path):
  transcription = whisper(file_path, return_timestamps= True)
  return transcription["text"]
