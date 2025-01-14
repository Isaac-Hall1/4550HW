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
    return books
@app.get("/books/{book_id}")
def getBookById(book_id:int):
    data = getData()
    books = data['books']
    for book in books:
        if book['id'] == book_id:
            return book
    return {"message": "Book not found"}
@app.get("/authors")
def getAuthors():
    data = getData()
    authors = data['authors']
    authors.sort(key=lambda x:x['id'])
    return authors
@app.get("/authors/{author_id}")
def getAuthorById(author_id:int):
    data = getData()
    authors = data['authors']
    for auth in authors:
        if auth['id'] == author_id:
            return auth
    return {"message": "author not found"}
@app.get("/authors/{author_id}/books")
def getAuthorsBooks(author_id:int):
    data = getData()
    books = data['books']
    retBooks = []
    for book in books:
        if book['author_id'] == author_id:
            retBooks.append(book)
    retBooks.sort(key=lambda x:x['id'])
    return retBooks
