from flask import Flask, render_template


app = Flask (__name__)

@app.route('/')
def homepage():
	title = "..."
	try:
		return render_template ("index.html", title = title)
	except Exception, e:	
		return str(e)

	
	    

if __name__ == "__main__":
    app.run('45.79.103.76')



