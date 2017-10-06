# URL Shortener Demo

Small demo of a URL shortening service - you put a long URL in, it gives you an abridged URL that redirects to your original one. Made as a trial-by-fire project for learning Flask and SQL... and it actually works!

Built with **Flask**, **SQLite**, and a dash of **Bootstrap**. Eventually I'd love to learn how to do this with Django and Redis, but that'll have to wait.

## Setup
Install SQLite3 (`sudo apt install sqlite3`) if you don't have it already. Clone this repository somewhere on your local machine, then use a virtualenv (`sudo apt install virtualenv` to install):

```
virtualenv urlshortener
source urlshortener/bin/activate
pip3 install -r requirements.txt
```

Then start the script with `python3 main.py`. This assumes you're running on localhost and your SQL database file is in the project root. If not, change those fields in `main.py`.

To leave your virtualenv, use the `deactivate` command.

## How does it work?
Although I structured the code to be readable, here's a quick explanation:

* `utils.py` contains methods for converting our database IDs into alphanumeric codes, and vice versa. Just your standard change-of-base code.
* `main.py` contains the actual Flask app. 
	* When we run the script, it first creates a table called `WEB_URL` in the database if it isn't there already. Then, it starts the app and begins accepting connections.
	* The `index()` method is set up to recieve user input from the textbox. When we recieve a `GET` request, we just serve out `index.html` as-is. However, when we recieve a `POST` request (aka data has been submitted) we add it to the database table, convert the ID to a code, and print out the new URL on the same `index.html` page.
	* `redirect_short_url(short_url)` can be reached with `localhost:5000/<short_url>`. It takes the short url - the stuff after the `/` - and converts it back to database ID form. It then looks up this ID in the table, and if it finds it, it'll redirect you to the original URL. If it doesn't find it, it'll just redirect to the index page - eventually it'd be nice to have a 404 page here.
* `templates/index.html` is the default page served - as specified in `index()`. Admittedly, the Bootstrap in it is pretty terrible, so don't look too hard at that.
	* Notice how the textfield has `id="url"`, that's how it hooks into the `request.form.get("url")` found in `index()`.
	* The new URL is displayed below the input field if it has been generated. Flask executes control clauses in HTML with `{%  %}`, and serves content like our new_url with `{{  }}` (as found in the link snippet.




