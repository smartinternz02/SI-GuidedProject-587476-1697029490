from flask import Flask, render_template, request

pediatric = Flask(__name__)

@pediatric.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    pediatric.run(debug=False, port = 8985)