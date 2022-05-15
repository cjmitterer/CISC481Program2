from flask import Flask, request, render_template
import puzzles
import json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from main import urlToBoard, puzzleConverter, backTrackingSearch, nineXNineConstraints

#app = Flask("Sudoku")
app = Flask(__name__)

"""
class EnterBoard(FlaskForm):
    puzzleValue = StringField("Enter a Puzzle")
    submit = SubmitField("Submit Puzzle")
"""

"""
@app.route('/puzzle', methods=['GET', 'POST'])
def puzzleQuery():
        puzzleValue = None
        form = EnterBoard()

        return render_template("PuzzlePrompt.html", puzzleValue = puzzleValue, form = form)
"""
@app.route('/')
def index():
    return render_template('WebDev.html')

@app.route('/submit')
def submit():
    args = request.args
    if "board" in args:
        board = args.get("board")
        print(board)

        dictBoard = urlToBoard(board)
        print(dictBoard)

        dictBoard = puzzleConverter(dictBoard)
        print(dictBoard)

        #dictBoard = puzzleConverter(puzzles.puzzleOne)

        #print(len(nineXNineConstraints))
        submittedSolution, _ = backTrackingSearch(nineXNineConstraints, dictBoard)

        keys = []
        vals = []
        for x in submittedSolution:
            keys.append(str(x[1:]))
            vals.append(str(submittedSolution[x][0]))
        print(keys)


    return render_template('DisplayPuzzle.html', locations = keys, vals = vals)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run()
