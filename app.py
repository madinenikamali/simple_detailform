from flask import Flask, render_template, request, redirect
import sqlite3
app = Flask(__name__)
def get_db_connection():
    return sqlite3.connect('contacts.db')
@app.route('/')
def index():
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    con.close()
    return render_template("index.html", contacts=contacts)
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        data = (
            request.form['first_name'],
            request.form['last_name'],
            request.form['address'],
            request.form['email'],
            request.form['phone']
        )
        con = get_db_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO contacts (first_name, last_name, address, email, phone) VALUES (?, ?, ?, ?, ?)", data)
        con.commit()
        con.close()
        return redirect('/')
    return render_template("add.html")
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    con = get_db_connection()
    cur = con.cursor()
    if request.method == 'POST':
        data = (
            request.form['first_name'],
            request.form['last_name'],
            request.form['address'],
            request.form['email'],
            request.form['phone'],
            id
        )
        cur.execute("UPDATE contacts SET first_name=?, last_name=?, address=?, email=?, phone=? WHERE id=?", data)
        con.commit()
        con.close()
        return redirect('/')
    cur.execute("SELECT * FROM contacts WHERE id=?", (id,))
    contact = cur.fetchone()
    con.close()
    return render_template("edit.html", contact=contact)
@app.route('/delete/<int:id>')
def delete_contact(id):
    con = get_db_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
