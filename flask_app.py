
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Beranda"
    user = {'username': 'Andromeda'}
    return render_template('index.html',
                            title=title,
                            user=user
    )


@app.route('/lapkeu')
def lapkeu():
    title = "Laporan Keuangan"
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('lapkeu.html',
                            title=title,
                            comments=comments
    )