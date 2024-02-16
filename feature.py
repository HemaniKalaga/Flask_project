from flask import Flask
FAIO=Flask(__name__)

@FAIO.route('/stringResponse')
def stringResponse():
    return 'This is 1st project in flask'

if __name__ == '__main__':
    FAIO.run(debug=True)
