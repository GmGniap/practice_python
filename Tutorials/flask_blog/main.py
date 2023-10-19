from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = '0e748eccc059ded6ce6e0d7cb3f6b302'   ## need for security (WTForms)
import routes

if __name__ == "__main__":
    app.run(debug=True)
