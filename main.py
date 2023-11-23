from flask import Flask , render_template
import random
import openai

app = Flask(__name__)

que = "Tell me one sentence joke."
ans = "a"


@app.route("/")
def main():
    # name = "ved"
    randomno = random.randint(100, 500)
    # print(randomno)

    
    def ChatGPTComm():    

        # openai.api_key  = os.getenv('OPENAI_API_KEY')
        _api_key = "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"
        # print("api key: ###" + _api_key + "###")

        openai.api_key = _api_key # Replace 'your-api-key' with your actual OpenAI API key

        def get_completion(prompt, model="gpt-3.5-turbo"):
            messages = [{"role": "user", "content": prompt}]
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0, # this is the degree of randomness of the model's output
            )
            return response.choices[0].message.content

        # prompt = f"""
        # Tell me one sentence joke.
        # """
        prompt = que

        response = get_completion(prompt)

        # print(response.choices[0].message.content)
        # print(response)

        return response

    ans = ChatGPTComm()
    return render_template('index.html', namevar=randomno, que=que, ans=ans)

# @app.route("/ved")
# def ved():
#     return "<p>SSB page</p>"

app.run(debug=True) # debug=True - automatic refresh

