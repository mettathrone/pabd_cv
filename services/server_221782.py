from flask import Flask

app = Flask('Image classifier')


@app.route('/')
def home():
    return 'Home page'


if __name__ == '__main__':
    app.run(port=1782)        #номер зачетки
    input()
