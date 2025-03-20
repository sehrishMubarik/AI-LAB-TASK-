from flask import Flask, render_template
import requests

app = Flask(__name__)

spoonacular_API = "48529b8e82b44be094b648cb7a4409c6"
APOD_URL = "https://api.spoonacular.com/recipes/random"


@app.route("/", methods=["GET"])
def index():
    par = {"apiKey": spoonacular_API}  # Fixed API key parameter
    response = requests.get(APOD_URL, params=par)
    
    print("API Response Status:", response.status_code)
    print("API Response Content:", response.text)  # Debugging step

    apod_data = response.json()
    return render_template("index.html", apod=apod_data)


# @app.route("/", methods=["GET"])
# def index():
#     par = {"api_key" : spoonacular_API}
#     response = requests.get(APOD_URL, params=par)
#     apod_data = response.json()
#     return render_template("index.html", apod = apod_data)

if __name__ == "__main__":
    app.run(debug=False)