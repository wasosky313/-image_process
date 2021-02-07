import uvicorn


from app_01 import start_app

app = start_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, log_level="info", debug=True)
