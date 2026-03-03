from fastapi import FastAPI

app = FastAPI(title="Watchlist API")

@app.get("/health")
def health():
    return {"ok": True}