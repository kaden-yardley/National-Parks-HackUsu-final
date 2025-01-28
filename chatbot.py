import openai
import datetime

# Prompt template for generating park recommendations
recommender_prompt_wrapper = """\
Write 5 recommendations for cool things to do for the following national park:\n{input}\nPlease do it in bullet point form with no text before or after the bullet points,\nremember that the month is {date} and there might be weather restrictions due to this.\n"""

def set_openai_key(key: str):
    """Sets the OpenAI API key."""
    openai.api_key = key

class GeneralModel:
    def __init__(self):
        print("Model Initialization...")

    def query(self, prompt: str):
        """Calls the ChatCompletion API in a simple manner, similar to OpenAI docs."""
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message["content"]

    def model_prediction(self, input_text: str, api_key: str) -> str:
        """Generates 5 recommendations for activities to do in a specific park, using a simplified approach."""
        current_month = datetime.datetime.now().month
        set_openai_key(api_key)
        prompt = recommender_prompt_wrapper.format(input=input_text, date=current_month)
        return self.query(prompt)
