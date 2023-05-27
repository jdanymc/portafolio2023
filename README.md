# Inicializar proyecto
```
python3 -m venv venv
source venv/lib/activate
pip install -r requirements.txt
```
# Si no funciona el comando `flask run` ejecutar los siguientes comandos:
```
export FLASK_APP=run.py
export FLASK_DEBUG=True
```