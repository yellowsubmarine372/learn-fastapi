from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from containers import Container
from user.interface.controllers.user_controller import router as user_routers
from example.ch06_02.sync_ex import router as sync_ex_routers
from example.ch06_02.async_ex import router as async_ex_routers

app = FastAPI()
container = Container()
container.wire(
    packages=["user"],
    modules=["user.interface.controllers.user_controller"]
)

app.container = container
app.include_router(user_routers)
app.include_router(sync_ex_routers)
app.include_router(async_ex_routers)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.exception_handler(RequestValidationError)

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content=exc.errors()
    )