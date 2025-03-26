import getpass
import os
from langchain.chat_models import init_chat_model

import os
from groq import Groq
GROQ_API_KEY = "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"

def model(text, api_key=GROQ_API_KEY):

  client = Groq(
      api_key=api_key,
  )

  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": f"Summerize this text {text} between the lower word linit of 30 and upper word limit of 170",
          }
      ],
      model="gemma2-9b-it",
  )

  return chat_completion.choices[0].message.content

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = GROQ_API_KEY

def model2(text):
  model = init_chat_model("llama3-8b-8192", model_provider="groq")
  message = model.invoke(f"Summerize this text {text} between the lower word linit of 30 and upper word limit of 170")
  return message.content