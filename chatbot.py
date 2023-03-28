import openai
import datetime



recommender_prompt_wrapper = """Write 5 recommendations for cool things to do for the following national park: 
{input}
Please do it in bullet point form with no text before or after the bullet points,
remember that the month is {date} and there might be weather restrictions due to this.
"""

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "engine": "gpt-3.5-turbo",
            "messages": {"role": "user", "content": prompt},
            "temperature": 0.25,
            "max_tokens": 200,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["###"],
        }


        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]


        r = openai.ChatCompletion.create(model= "gpt-3.5-turbo",
  messages= [{"role": "user", "content": prompt}])["choices"][0]
        return r

    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        current_date = datetime.datetime.now().month
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(recommender_prompt_wrapper.format(input = input, date = current_date))
        return output