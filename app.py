from flask import Flask, request, jsonify

app = Flask(__name__)

# def create_app():
#     return app

@app.route('/sum', methods=["POST"])
def sum():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'result': result})

# if __name__ == '__main__':
#     app = create_app()

#     app.run(debug=True)