from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/")
async def test(request):
    return json({"hello": "async world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, workers=4)
