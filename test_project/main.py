from fastapi import FastAPI
from elrahapi.middleware.error_middleware import ErrorHandlingMiddleware
from elrahapi.middleware.log_middleware import LoggerMiddleware
# from .myapp.router import app_myapp
from .settings.models_metadata import database
from .settings.logger.router import logger_router
from .settings.logger.model import Log
from .settings.auth.configs import authentication_router
from .settings.auth.routers import user_router, role_router,user_role_router,user_privilege_router,privilege_router,role_privilege_router
app = FastAPI()


@app.get("/bakek")
async def hello():
    return {"message":"hello"}

app.include_router(authentication_router)
app.include_router(user_router)
app.include_router(role_router)
app.include_router(user_role_router)
app.include_router(privilege_router)
app.include_router(user_privilege_router)
app.include_router(role_privilege_router)
# app.include_router(app_myapp)
app.include_router(logger_router)
app.add_middleware(
    LoggerMiddleware, LogModel=Log, session_manager=database.session_manager
)
app.add_middleware(
    ErrorHandlingMiddleware, LogModel=Log, session_manager=database.session_manager
)
