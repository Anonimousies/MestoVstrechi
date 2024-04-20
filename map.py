from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def render_map():        
    return render_template('map.html', cord1 = 59.82373565, cord2 = 30.083922400000006)	
	
if __name__ == '__main__':
    app.run(debug = True)
