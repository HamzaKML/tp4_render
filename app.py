from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
  return "TP4 : Bonjour depuis Render ! Votre app Flask est bien en ligne..... #2nd Commit test#"

if __name__ == '__main__':
  app.run()
