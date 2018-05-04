import os
import subprocess
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	jsonData = request.json
	if jsonData:
		return 'Hello, you supplied {} from {}!'.format(jsonData['name'], jsonData['source'])
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
