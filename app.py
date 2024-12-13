
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

servers = []

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        ip = request.form['ip']
        server = {'id': len(servers), 'name': name, 'ip': ip}
        servers.append(server)
        return redirect(url_for('index'))
    return render_template('index.html', servers=servers)

if __name__ == '__main__':
    app.run(debug=True)
