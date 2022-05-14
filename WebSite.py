from flask import Flask
from flask import render_template
app = Flask("Sudoku")

@app.route("/<board>")
def query():
    return render_template('WebDev.html', boards=boards)