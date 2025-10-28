from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    reg_no = request.form['reg_no']
    # Just for testing
    result_data = {“SANS001”: “Passed”, “SANS002”: “Failed”}
    result = result_data.get(reg_no.upper(), “Result not found”)
    return render_template('result.html', reg_no=reg_no, result=result)

if __name__ == “__main__”:
    app.run(debug=True)
  
