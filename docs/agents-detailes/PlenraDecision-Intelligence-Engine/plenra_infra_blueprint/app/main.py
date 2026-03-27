from fastapi import FastAPI

from app.api.routes import router
from app.config import settings
from app.logging_config import configure_logging

configure_logging()

app = FastAPI(title=settings.app_name)
app.include_router(router, prefix=settings.api_prefix)
