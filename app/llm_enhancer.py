from app.config import GOOGLE_API_KEY

def enhance_with_llm(readme_text):

    if not GOOGLE_API_KEY:
        return readme_text

    try:
        from google import genai
        client = genai.Client(api_key=GOOGLE_API_KEY)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Improve clarity only. Do not add new features.\n\n" + readme_text
        )

        return response.text

    except:
        return readme_text
