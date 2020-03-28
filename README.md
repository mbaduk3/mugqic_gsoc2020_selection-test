# mugqic_gsoc2020_selection-test
Google Summer of Code 2020.\
Organization: Canadian Centre for Computational Genomics.\
Project: "Ingesting the Canadian Common CV" -- selection test.\

This small webapp provides certain endpoints for the serving of bioinformatics.stackexchange.com post data, with a few filtering options.

To run, install requirements using 
`pip install -r requirements.txt`.
Then, run
`python app.py`
to launch the server.

Valid GET endpoints include:
- `localhost:5000/posts?sortBy=<view|score|chron>` to get all sorted posts.
- `localhost:5000/posts/search?term=<term>` to search all posts' title and body for `term`.
