
from api import app

app = app

if __name__ == "__main__":
    app.debug = False
    app.run()