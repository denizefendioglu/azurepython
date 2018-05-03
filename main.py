import os
import subprocess
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	name = request.args.get('name', default='', type=str)
	if len(name) > 0:
		return 'Hello, {}!'.format(name)
	else:
		return 'Hello, world!'

@app.route('/exec')
def exec_script():
	try:
		dirname = os.path.dirname(__file__)
		output = subprocess.run([os.path.join(dirname, 'scripts', 'cmd.sh')], stdout=subprocess.PIPE).stdout.decode('utf-8')
		return 'Exec output: {}'.format(output)
	except Exception as e:
		return 'Exec error! {}'.format(e)

if __name__ == '__main__':
	app.run()
