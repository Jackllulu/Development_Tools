from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def hello():
    return {"message": "Hello, Flask"}


if __name__ == "__main__":
    app.run(debug=True)
