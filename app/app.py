from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello Meghana. This app is built for DevOps CI/CD pipeline."

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001)

