from fastapi import FastAPI, Request, HTTPException
from time import time
from collections import defaultdict

app = FastAPI()

# Rate limit settings
RATE_LIMIT = 100  # Max requests
WINDOW_SIZE = 60  # In seconds

# Dictionary to track request times per IP
request_log = defaultdict(list)

@app.middleware("http")
async def rate_limiter(request: Request, call_next):
    client_ip = request.client.host
    current_time = time()

    # Remove timestamps older than the window
    request_log[client_ip] = [
        ts for ts in request_log[client_ip]
        if current_time - ts < WINDOW_SIZE
    ]

    # Check if IP exceeded rate limit
    if len(request_log[client_ip]) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # Record current request
    request_log[client_ip].append(current_time)
    return await call_next(request)

@app.get("/")
def root():
    return {"message": "Hello, world! You are within the rate limit."}
