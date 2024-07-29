from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def indexhomework():
    response = requests.get("https://api.quotable.io/random")
    quote_data = response.json()
    quote = quote_data['content']
    author = quote_data['author']

    return render_template('indexhomework.html', quote=quote, author=author)



if __name__ == '__main__':
    app.run(debug=True)