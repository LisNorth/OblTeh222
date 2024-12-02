from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return render_template_string('''
    <html>
    <head><title>My App</title></head>
    <body>
    <h1>Hello, world!!!!!</h1>
    </body>
    </html>
    ''')


if __name__ == "__main__":
    app.run(port=5000)
