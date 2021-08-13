.\venv\Scripts\activate.ps1

pip install -r requirements.txt

python uvicorn main:app -p 8000 --reload