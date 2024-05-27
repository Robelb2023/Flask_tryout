from flask import Flask

#Maak een flask applicatie
app = Flask(__name__)

#Defineer een default-route
@app.route('/')
def hello_world():
    return "<p>Hello world!</p>"

if __name__=='__main__':
    app.run()