import sqlite3
import xml.etree.ElementTree as ET

"""
    This script ingests the data from 'bioinformatics_posts_se.xml' into a 
    sqlite database ('posts.db')
"""

conn = sqlite3.connect('posts.db')
c = conn.cursor()

create_table = """
    CREATE TABLE IF NOT EXISTS posts (
        id integer primary key, 
        postTypeId integer,
        parentId integer,
        creationDate text,
        score integer,
        viewCount integer, 
        body text,
        ownerUserId integer,
        lastActivityDate string,
        title string,
        commentCount integer
    );
"""
c.execute(create_table)

tree = ET.parse('bioinformatics_posts_se.xml')
root = tree.getroot()
for child in root:
    post = child.attrib
    needed = ['Id', 'PostTypeId', 'ParentId', 'CreationDate', 'Score', 
              'ViewCount', 'Body', 'OwnerUserId', 'LastActivityDate', 
              'Title', 'CommentCount']
    values = []
    for elem in needed:
        try:
            values.append(post[elem])
        except:
            values.append(None)
    c.execute('INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', values)

conn.commit()
conn.close()


