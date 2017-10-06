import utils
from flask import Flask, request, render_template, redirect
import sqlite3
try:
    from urllib.parse import urlparse  # Python 3
except ImportError:
    from urlparse import urlparse  # Python 2 (ugh)

host = 'http://localhost:5000/' # Change for deployment
database = 'database.db' # Change if database is named differently

# Creates a table if one doesn't exist already. Assumes
#   that your database (specified above) is in proj root.
def validate_table():
    create_table_cmd = """
        	CREATE TABLE WEB_URL(
        		ID INTEGER PRIMARY KEY AUTOINCREMENT,
        		URL TEXT NOT NULL
        	);
        """
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(create_table_cmd)
        except sqlite3.OperationalError as o:
        	pass

# Where the flasky stuff starts!
app = Flask(__name__)

# Home page where user should enter
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # Form has been submitted
        original_url = request.form.get('url')
        if urlparse(original_url).scheme == '':
            original_url = 'http://' + original_url
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()
            result_cursor = cursor.execute(
                "INSERT INTO WEB_URL (URL) VALUES ('" +
                 original_url + "')"
            )
            encoded_string = utils.convert_num_to_alpha(result_cursor.lastrowid)
        return render_template('index.html', new_url = host + encoded_string)
    else:
    	return render_template('index.html')

@app.route('/<short_url>') # Reached with <host>/<short_url>
def redirect_short_url(short_url):
    decoded_string = utils.convert_alpha_to_num(short_url)
    redirect_url = host # Fallback, in case ID can't be found
    with sqlite3.connect(database) as connection:
        cursor = connection.cursor()
        result_cursor = cursor.execute(
        	"SELECT URL FROM WEB_URL WHERE ID=" + str(decoded_string)
        )
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print(e)
    return redirect(redirect_url)


if __name__ == '__main__':
    validate_table()
    app.run(debug=True)