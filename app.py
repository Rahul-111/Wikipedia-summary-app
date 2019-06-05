from flask import Flask ,request,render_template
import wikipedia
app = Flask(__name__)

# @app.route('/')
# def index():
# 	query=request.args.get('query')
# 	return render_template('index.html',query=query)
@app.route("/",methods=['GET','POST'])
def login():
	if request.method=="GET":
		return render_template('login.html')
	else:
		querystr=request.form.get('query')
		ans=wikipedia.summary(querystr)
		return render_template('index.html',weki=ans)

if __name__ == '__main__':
   app.run(use_reloader=True ,debug=True)