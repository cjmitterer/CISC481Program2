from flask import Flask, request
from flask import render_template
from main import urlToBoard, puzzleConverter, backTrackingSearch, nineXNineConstraints

app = Flask("Sudoku")

@app.route("/submit")
def query():
    args = request.args
    if "board" in args:
        board = args.get("board")
        dictBoard = puzzleConverter(urlToBoard(board))
        backTrackingSearch(nineXNineConstraints, dictBoard)