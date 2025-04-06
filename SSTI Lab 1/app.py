from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    profile_info = {
        'username': 'MrWebSecure',
        'bio': 'Cybersecurity Enthusiast | Ethical Hacker | Exploring Vulnerabilities',
        'location': 'Maharashtra, India',
        'website': 'https://mrwebsecure.com'
    }
    user_input = ""

    if request.method == 'POST':
        profile_info['username'] = request.form.get('username')
        profile_info['bio'] = request.form.get('bio')
        profile_info['location'] = request.form.get('location')
        profile_info['website'] = request.form.get('website')
        user_input = request.form.get('vulnerable_field')

        try:
            # Now the input is directly passed to render_template_string
            output = render_template_string(user_input)
        except Exception as e:
            output = f"Error: {str(e)}"

    return render_template('index.html', profile_info=profile_info, output=output)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
