import LSA
from datetime import timedelta
from flask import Flask,make_response, request, current_app, jsonify
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
	origin = ', '.join(origin)
	def get_methods():
		if methods is not None:
			return methods
		options_resp = current_app.make_default_options_response()
		return options_resp.headers['allow']

	def decorator(f):
		def wrapped_function(*args, **kwargs):
			
			h['Access-Control-Allow-Methods'] = get_methods()
			h['Access-Control-Max-Age'] = str(max_age)
			if headers is not None:
			    h['Access-Control-Allow-Headers'] = headers
			return resp

			f.provide_automatic_options = False
			return update_wrapper(wrapped_function, f)
		return decorator

app = Flask(__name__)
theLSA = LSA.LSA()
@app.route('/sumDoc', methods = ['POST'])
def summarize():
	print 'printed'
	resp = current_app.make_default_options_response()
	h = resp.headers
	h['Access-Control-Allow-Origin'] = '*'
	#print request.form['aDoc']
	#myValues = request.get_json(force=True)
	#print myValues
	resp.data= theLSA.sumDoc(request.form['aDoc'])
	return resp

	

if __name__ == '__main__':
	app.debug = True
	app.run()