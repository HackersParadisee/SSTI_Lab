from flask import Flask, render_template, request, redirect, session
from markupsafe import Markup
from jinja2 import Template

app = Flask(__name__)
app.secret_key = 'ssti_demo_secret'

@app.route('/')
def index():
    ssti_enabled = session.get('ssti_enabled', False)
    return render_template('create_event.html', ssti_enabled=ssti_enabled)

@app.route('/event', methods=['POST'])
def event():
    event_name = request.form['event_name']
    date = request.form['date']
    location = request.form['location']
    description = request.form['description']
    ssti_enabled = session.get('ssti_enabled', False)

    if ssti_enabled:
        try:
            template = Template(description)
            description = Markup(template.render())
        except:
            description = Markup("<strong>⚠️ SSTI Error</strong>")

    return render_template('event_details.html',
                           event_name=event_name,
                           date=date,
                           location=location,
                           description=description,
                           ssti_enabled=ssti_enabled)

@app.route('/toggle_ssti', methods=['POST'])
def toggle_ssti():
    session['ssti_enabled'] = not session.get('ssti_enabled', False)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
