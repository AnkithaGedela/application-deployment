from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')  # Default to localhost if not set
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')  # Default user
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', '')  # Default to empty string
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'test')  # Default database name

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)  # Explicitly set the port
