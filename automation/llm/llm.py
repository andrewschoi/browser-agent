from dotenv import load_dotenv
import openai
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class LLM:
    def __init__(self, model="gpt-3.5-turbo"):
        self.chat_completion = openai.ChatCompletion
        self.model = model

    def ask(self, question):
        return (
            self.chat_completion.create(
                model=self.model, messages=[{"role": "user", "content": question}]
            )
            .choices[0]
            .message.content
        )
