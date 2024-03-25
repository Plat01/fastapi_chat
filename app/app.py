from fastapi import FastAPI, Depends

app = FastAPI(
    # dependencies=[Depends(get_db)]
)

# app.include_router(
#
# )


@app.get("/")
async def root():
    return {"message": "Hello World"}