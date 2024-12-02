from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return render_template_string('''
    <html>
    <head><title>My App</title></head>
    <body>
    <h2 style="color: red; font-style: italic;">Hello, world!!!!!</h2>
    </body>
    </html>
    ''')


if __name__ == "__main__":
    app.run(port=5000)
