from fastapi import FastAPI

app = FastAPI(title="Demo API")


@app.get("/hello")
def hello(name: str = "FastAPI") -> dict[str, str]:
    return {"message": f"Hello, {name}"}
