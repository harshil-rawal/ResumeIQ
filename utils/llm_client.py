"""
Gemini Client for ResumeIQ
"""

from google import genai

from utils.config import GEMINI_API_KEY


class GeminiClient:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt):
        """
        Generate response from Gemini.
        """

        try:

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"[Gemini Error] {e}")

            return None