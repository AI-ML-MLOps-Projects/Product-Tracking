import io
import os
import uvicorn # unicorn is a web server
# import numpy as np
import nest_asyncio
# from enum import Enum
from fastapi import FastAPI, UploadFile, File, HTTPException, WebSocket
from fastapi.responses import StreamingResponse, HTMLResponse

from pydantic import BaseModel
# import ws_server 
import asyncio
# import time
import datetime
# import websockets

# Assign an instance of the FastAPI class to the variable "app".
# You will interact with your api using this instance.
app = FastAPI(title='Deploying a ML Model with FastAPI')
# cfg = Context()

# By using @app.get("/") you are allowing the GET method to work for the / endpoint.
@app.get("/")
def home():
    return "Congratulations! Your API is working as expected. Now head over to http://localhost:8000/docs."

class Order(BaseModel):
    vehicle_number: str
    product_type: str
    product_quantity: int

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    while True:
        data_str = await websocket.receive_text()
        print("data : ", data_str)
        data_obj= eval(data_str)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        counter = 0
        print("counter : ", counter)
        total_count = int(data_obj['totalNum'])
        print("total count : ", total_count)

        while counter >= 0 and counter < total_count:
            counter += 1
            print("counter at now : ", counter)
            await websocket.send_text(f"Message text was: {counter}")
            await asyncio.sleep(1)
        
        # if counter >= total_count:
        #     print("counter reset : ", counter)
        #     counter = -1

# Allows the server to be run in this interactive environment
nest_asyncio.apply()
# Host depends on the setup you selected (docker or virtual env)
host = "0.0.0.0" if os.getenv("DOCKER-SETUP") else "127.0.0.1" #-> TODO
# Spin up the server!    
uvicorn.run(app, host=host, port=8000)
