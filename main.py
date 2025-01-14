"""Assignment #1 FastAPI application.

Args:
    app: The FastAPI instance

Usage:
    run `fastapi dev` or `poetry run fastapi dev` to start the server
"""

from fastapi import FastAPI
import json

app = FastAPI()

#gets all books
def getDataBooks():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data['books']

#gets all authors
def getDataAuthors():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data['authors']

#returns sorted data
def sortById(list):
    list.sort(key=lambda x:x['id'])
    return list

#returns all books
@app.get("/books")
def getBooks():
    books = getDataBooks()
    return sortById(books)

#returns specified book
@app.get("/books/{book_id}")
def getBookById(book_id:int):
    books = getDataBooks()
    for book in books:
        if book['id'] == book_id:
            return book
    return {"message": "Book not found"}

#returns all authors
@app.get("/authors")
def getAuthors():
    authors = getDataAuthors()
    return sortById(authors)

#returns specified author
@app.get("/authors/{author_id}")
def getAuthorById(author_id:int):
    authors = getDataAuthors()
    for auth in authors:
        if auth['id'] == author_id:
            return auth
    return {"message": "author not found"}

#returns books from specified author
@app.get("/authors/{author_id}/books")
def getAuthorsBooks(author_id:int):
    books = getDataBooks()
    retBooks = []
    for book in books:
        if book['author_id'] == author_id:
            retBooks.append(book)
    return sortById(retBooks)
