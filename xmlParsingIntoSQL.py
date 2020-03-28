import xml.etree.ElementTree as ET 
import sqlite3

conn = sqlite3.connect('bookdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS AUTHOR
DROPTABLEIFEXISTS TITLE
DROPTABLE IF EXISTS YEAR
DROP TABLE IF EXISTS CATEGORY
DROPTABLE IF EXISTS PRICE

CREATE TABLE Author()
CREATE TABLE Title
CREATE TABLE Year
CREATE TABLE Category
CREATE TABLE Price

''')


tree = ET.parse('books.xml') #parsing the XML data into an element tree

booklist = tree.findall('book') #creating a list of the wanted child elements 


print("Bookcount:", len(booklist)) # printing the amount of the wanted child elements - in this case books

for book in booklist: #printing the information for every book in the list
	print('Author:', book.find('author').text)
	print('Title:', book.find('title').text)
	print('Year:', book.find('year').text)
	print('Category:', book.attrib['category'])
	print('Price:', book.find('price').text)
	
	
