import sqlite3
from time import strftime
from datetime import datetime
from datetime import date
try:
	import pyperclip
except:
	pass
import os
import sys
import time
import webbrowser

conn = sqlite3.connect('todo.db')
c = conn.cursor()
try:
	c.execute("""CREATE TABLE todo(
	    todo text,
	    status text,
	    time_ text
	)""")
except:
	pass

def time_cal():
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    timeAnddate = (f'{current_t_f} {current_date}')
    return timeAnddate

def add_to_db(todo_):
	c.execute("INSERT INTO todo VALUES (:todo, :status, :time_)",
		{
			'todo': todo_,
			'status': 'pending',
			'time_': time_cal()
		})
	conn.commit()
	print("added given todo")

def show_db():
	c.execute('SELECT rowid, * FROM todo')
	raw_db_content = c.fetchall()
	print("INDEX \t   TODO \t Status \t TIME")
	for todo in raw_db_content:
		print(f'  {todo[0]}   | {todo[1]} | {todo[2]} | {todo[3]}')

def quit_topy():
	print("Thanks for using ToPy - ToDo Py get it??\nBy NoobScience")
	exit()

def mark(index):
	c.execute("UPDATE todo SET status = 'done' WHERE rowid = :rowid",{
		'rowid': index,
		})
	c.execute("SELECT * FROM todo")
	conn.commit()
	print("Marked off given index")

def unmark(index):
	c.execute("UPDATE todo SET status = 'pending' WHERE rowid = :rowid",{
		'rowid': index,
		})
	c.execute("SELECT * FROM todo")
	conn.commit()
	print("Given index is now marked pending")

def del_marked():
	c.execute("DELETE from todo WHERE status = 'done'")
	print("Deleted all ToDo's with done status")

def clear_terminal():
	try:
		os.system("clear")
	except:
		os.system("cls")
	print("ToPy - The CLI Todo Manager")

def destroy_db():
	c.execute("DELETE from todo")
	print("Deleted all ToDo's")

print("ToPy - The CLI Todo Manager")
while True:
	command = (str.lower(input("> "))).replace(" ", "")
	if command == "new":
		todo_to_add = str(input("Enter the TODO: "))
		add_to_db(todo_to_add)
	if command == "n":
		todo_to_add = str(input("Enter the TODO: "))
		add_to_db(todo_to_add)
	if command == "show":
		show_db()
	if command == "quit":
		quit_topy()
	if command == "mark":
		show_db()
		todo_to_mark = int(input("Insert the index you want to mark off: "))
		mark(todo_to_mark)
	if command == "unmark":
		show_db()
		todo_to_mark_pending = int(input("Insert the index you want to mark pending: "))
		unmark(todo_to_mark_pending)
	if command == "del":
		del_marked()
	if command == "clear":
		clear_terminal()
	if command == "ls":
		show_db()
	if command == "read":
		show_db()
	if command == "destroy":
		destroy_db()
	if command == "license":
		file = open("LICENSE", 'r')
		print(file.read())
	if command == "about":
		file = open("about.txt", 'r')
		print(file.read())
	if command == "help":
		file = open("README.txt", 'r')
		print(file.read())
	if command == "commands":
		file = open("commands.txt", 'r')
		print(file.read())
	if command == "website":
		x = input("Opening the website: Press Enter to continue")
		webbrowser.open("https://newtoallofthis123.github.io/topy")
	if command == "github":
		x = input("Opening the website: Press Enter to continue")
		webbrowser.open("https://github.com/newtoallofthis123/topy")
	if command == "docs":
		x = input("Opening the website: Press Enter to continue")
		webbrowser.open("https://newtoallofthis123.github.io/topy/docs.html")