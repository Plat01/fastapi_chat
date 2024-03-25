import uvicorn
from app.config import settings

if __name__ == '__main__':
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, log_level=settings.LOG_LEVEL)
