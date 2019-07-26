from gingerit.gingerit import GingerIt

from flask import Flask,request,render_template
#from flask_restful import Api

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    comment = request.form['comment']
    parser=GingerIt()
    x=parser.parse(comment)
    s=x['result']
    return render_template('result.html',pred=s)
if __name__ == '__main__':
    app.run(port=5000, debug=True)  # important to mention debug=True
