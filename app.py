from flask import Flask, render_template
from src.Application.Controllers.CategoryController import category_controller
app = Flask(__name__, template_folder='templates', static_folder='static')
import psycopg2

app.register_blueprint(category_controller)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
