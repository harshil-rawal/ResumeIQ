from utils.llm_client import GeminiClient


def test_gemini_connection():

    client = GeminiClient()

    response = client.generate(
        "Say hello in one sentence."
    )

    assert isinstance(response, str)
    assert len(response) > 0