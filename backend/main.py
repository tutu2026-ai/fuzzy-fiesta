from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from subapase import create_client, client
import os

app = FastAPI()

# Critical : Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Change this to your Vercel URL later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Supabase
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://neyiayemuqazgtgxbmzn.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "neyiayemuqazgtgxbmzn")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.get("/items")
def get_items():
    # Fetch data from your Supabase DB
    response = supabase.table('items').select("*").execute()
    return response.data