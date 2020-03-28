from flask import Flask, jsonify, request, redirect
import sqlite3
import re

"""
    This script launches the webapp which serves data from the 'posts.db' 
    database
"""

app = Flask(__name__)

# Returns the posts, sorted by view count, score, or creation date (default).
@app.route('/posts/', methods=["GET"])
def get_posts():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    sortBy = request.args.get('sortBy')
    if (sortBy == "view"):
        query = "SELECT * FROM posts ORDER BY viewCount DESC"
    elif (sortBy == "score"):
        query = "SELECT * FROM posts ORDER BY score DESC"
    else:
        query = "SELECT * FROM posts ORDER BY creationDate DESC"
    rows = []
    for row in cur.execute(query):
        rows.append(row)
    conn.close()
    return jsonify(rows)

# Searches the posts' body and title for a key term.
@app.route('/posts/search/', methods=['GET'])
def search_posts():
    conn = sqlite3.connect('posts.db')
    cur = conn.cursor()
    term:str = request.args.get('term')
    query = f"""
        SELECT * FROM posts WHERE title LIKE \'%{term}%\' OR body LIKE \'%{term}%\'
    """
    if (re.search("-{2}|;", query)):
        return "Invalid search string: " + term
    rows = []
    for row in cur.execute(query):
        rows.append(row)
    conn.close()
    return jsonify(rows)



if __name__ == "__main__":
    app.run(debug=True)

