from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)