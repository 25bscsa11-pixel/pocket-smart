import os
import json
import re
import base64
import shutil
import urllib.parse

from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
    File,
    UploadFile
)

from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from typing import List, Optional, Dict, Any, Union

from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

from PIL import Image
from io import BytesIO

import google.generativeai as genai
from dotenv import load_dotenv

import asyncio
from typing import Dict, Any, List, Optional
import uuid