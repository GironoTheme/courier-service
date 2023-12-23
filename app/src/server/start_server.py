from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from database.db_manager import base_manager
from groups import router as order_router
from app.src.server.clients import router as clients_router
from users import router as users_router
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_PRIMARY_DATA_PATH

app = FastAPI()

app.include_router(users_router, prefix='/users')
app.include_router(order_router, prefix="/groups")
app.include_router(clients_router, prefix='/app')


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_PRIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)


