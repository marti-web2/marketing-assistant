# from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keywords
# from mangum import Mangum
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()
# handler = Mangum(app)
MAX_INPUT_LENGTH = 32

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
  return


# @app.get("/generate_keywords")
async def generate_keywords_api(prompt: str):
  return


# @app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
  return


def validate_input_length(prompt: str):
  pass