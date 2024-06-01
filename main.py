from dotenv import load_dotenv
from flet import app
from tulify import Tulify


if __name__ == '__main__':
    load_dotenv()  # Variables de entorno cargadas
    app(target=Tulify)  # "mainloop"
