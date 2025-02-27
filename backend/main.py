from fastapi import FastAPI , HTTPException
from fastapi . middleware . cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv ()

# Initialize FastAPI
app = FastAPI ( title =" Learning AI Methods ")

# Configure CORS
app . add_middleware (
CORSMiddleware ,
allow_origins =[" http :// localhost :3000"] ,
allow_credentials = True ,
allow_methods =["*"] ,
allow_headers =["*"] ,
)

# Define data models
class TextInput ( BaseModel ) :
    text : str

# Root endpoint
@app . get ("/")
def read_root () :
    return {"message": " Learning AI Methods API "}

# AI processing endpoint
@app . post ("/api/summarize")


async def summarize_text ( input_data : TextInput ) :
# Simple integration with Hugging Face Inference API
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    headers = {"Authorization":f" Bearer {os.getenv('HF_API_KEY', '')}"}

    try :
        response = requests . post (
        API_URL ,
        json ={"inputs": input_data.text ,"parameters": {"max_length": 100}}

    )
        return {" result ": response . json () [0][" summary_text "]}
    except Exception as e :
        raise HTTPException ( status_code =500 , detail = str ( e ) )