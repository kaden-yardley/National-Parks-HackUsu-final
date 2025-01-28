import openai
import datetime

# Prompt template for generating park recommendations
recommender_prompt_wrapper = """\
Write 5 recommendations for cool things to do for the following national park:\n{input}\nPlease do it in bullet point form with no text before or after the bullet points,\nremember that the month is {date} and there might be weather restrictions due to this. Please include a note after the bullet points to always check current conditions for closures.\n"""

def set_openai_key(key: str):
    """Sets the OpenAI API key."""
    openai.api_key = key

class GeneralModel:
    def __init__(self):
        print("Model Initialization...")

    def query(self, prompt: str):
        """Calls the ChatCompletion API in a manner that returns a dict with 'message' content."""
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        # Return the first choice, which includes the 'message' dict
        return completion["choices"][0]

    def model_prediction(self, input_text: str, api_key: str) -> dict:
        """Generates 5 recommendations for activities to do in a specific park, returning dict structure."""
        # Set the OpenAI API key
        set_openai_key(api_key)
        # Get current month
        current_month = datetime.datetime.now().month
        # Format the prompt
        prompt = recommender_prompt_wrapper.format(input=input_text, date=current_month)
        # Query the model
        return self.query(prompt)
