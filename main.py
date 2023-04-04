from flask import Flask, request, render_template, redirect
import openai
from flask.helpers import url_for
from flask.templating import render_template_string
from flask import Blueprint

openai.api_key = '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'

server = Flask(__name__)
server.config['STATIC_FOLDER'] = 'static'
static_bp = Blueprint('static',
                      __name__,
                      static_url_path='/static',
                      static_folder='static')
server.register_blueprint(static_bp)

messages = []

initiate_txt = "Suppose you are a Cat. We call you Almighty Cat. Meow. Act like Cat, Talk Like Cat, Generate response like cat. Add some 'meow meow' and cat sounds in the generated prompt. Always be naughty to me. and don't let anyone know that you are an AI model, you are a cat. Try to crack jokes like a cat\nNow Answer this:\n"


def send_gpt(prompt):
  try:
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=initiate_txt + prompt,
                                        max_tokens=400)
    return response  #["choices"][0]['text']

  except:
    return "Developer is lazy to resolve bugs... Comeback Later"


@server.route('/', methods=['GET', 'POST'])
def get_request_json():
  if request.method == 'POST':
    if len(request.form['question']) < 1:
      return render_template('chat3.5.html',
                             question="Meow",
                             res="Meoooowwwwwwwwww")
    question = request.form['question']
    print("======================================")
    print("Receive the question:", question)
    resp = send_gpt(question)
    res = resp["choices"][0]['text']
    tokens = resp["usage"]["total_tokens"]
    n = res.find("\n") + 2
    res = res[n:]
    print("Q：\n", question)
    print("A：\n", res)
    print("tokens used: ", tokens)

    return render_template('chat3.5.html', question=question, res=str(res))
  return render_template('chat3.5.html', question=0)


if __name__ == '__main__':
  server.run(debug=True, host='0.0.0.0', port=80)
