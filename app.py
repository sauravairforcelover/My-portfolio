from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    # In a real app, you'd send an email or save to DB
    print(f"Message from {data.get('name')}: {data.get('message')}")
    return jsonify({"status": "success", "message": "Thank you! I'll get back to you soon."})

if __name__ == '__main__':
    app.run(debug=True)
