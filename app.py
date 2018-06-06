#!/usr/bin/python


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('Output.html')
if __name__ == '__main__':
    app.run()