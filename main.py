from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from user.interface.controllers.user_controller import router as user_routers

app = FastAPI()
app.include_router(user_routers)

@app.exception_handler(RequestValidationError)

@app.get("/")
def read_root():
    return {"Hello": "World"}

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content=exc.errors()
    )