"""Assignment #1 FastAPI application.

Args:
    app: The FastAPI instance

Usage:
    run `fastapi dev` or `poetry run fastapi dev` to start the server
"""

from fastapi import FastAPI
import json

app = FastAPI()


def getData():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/books")
def getBooks():
    data = getData()
    books = data['books'] 
    books.sort(key=lambda x:x['id'])
    return {"Books": books}
@app.get("/books/{book_id}")
def getBookById(book_id:int):
    data = getData()
    book = data['books'][book_id]
    return {'Book': book}
@app.get("/authors")
def getAuthors():
    data = getData()
    authors = data['authors']
    authors.sort(key=lambda x:x['id'])
    return {'Authors': authors}
@app.get("/authors/{author_id}")
def getAuthorById(author_id:int):
    data = getData()
    author = data['authors'][author_id]
    return {'Author': author}
@app.get("/authors/{author_id}/books")
def getAuthorsBooks(author_id:int):
    data = getData()
    books = data['books']
    retBooks = []
    for book in books:
        if book['author_id'] == author_id:
            retBooks.append(book)
    retBooks.sort(key=lambda x:x['id'])
    return {'AuthorBooks': retBooks}
