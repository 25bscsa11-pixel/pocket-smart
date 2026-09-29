# FastAPI app initialization
app = FastAPI(title="PocketSmart: AI Budget...")

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30