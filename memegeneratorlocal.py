import requests, random

hehe = ["Programming", "Gaming", "Life", "Relatable", "Random"]
motivation = ["Dajesz rade", "Nie poddawaj się", "Popłacz, pośmiej się, kawa i do roboty", "Będzie lepiej:)", "Dobra, Jeszcze jeden mem"]

def get_random_meme(arg=random.choice(hehe)):
    print(arg)
    try:
        response = requests.get(f"https://meme-api.com/gimme/{arg}")
        data = response.json()
        return data["url"]
    except:
        response = requests.get("https://meme-api.com/gimme/")
        data = response.json()
        return data["url"]


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    content = f"""
<html>
<body>
    <strong>{random.choice(motivation)}</strong>
    <img src="{get_random_meme()}"
    width="400"
    alt="gif"
    style="display:block;border:0;">
</body>
</html>
"""
    return content

if __name__ == "__main__":
    app.run(debug=True)