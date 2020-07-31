from flask import Flask
import sqlite3

database = "jobs_git.db"
app = Flask(__name__)


@app.route("/")
def create_web():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        tags = []
        cursor.execute("select name, url from JOBS")
        for title, url in cursor.fetchall():
            tag = "<div><a href = {}>{}</a></div>".format(url, title)
            tags.append(tag)

        result = (
            "<html><head><title>Jobs IT</title>"
            "<style>a {text-decoration: none;"
            "line-height: 2;}"
            "a:hover {color: blue;}</style></head>"
            "<body>IT JOBS" + "\n".join(tags) + "</body></html>"
        )

    return result


if __name__ == "__main__":
    app.run(debug=True)
