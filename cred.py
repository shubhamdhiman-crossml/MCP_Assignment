"""
Google API Key Loader Module

This module loads environment variables from a `.env` file and retrieves
the Google API key required for authenticating requests to the
Google Gemini (Generative AI) service.

It ensures that the API key is available at runtime and raises an
explicit error if the key is missing, helping prevent silent
authentication failures.

Environment Variables:
    GOOGLE_API_KEY (str): API key for Google Generative AI services

Raises:
    ValueError: If GOOGLE_API_KEY is not found in the environment
"""

import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY is not found.")