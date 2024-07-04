from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    return render_template('index1.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
