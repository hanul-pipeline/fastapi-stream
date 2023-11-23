from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
from utils.update_data import *
 

router = APIRouter()

# update measurement
# confirmed
@router.post('/update/100', response_class=PlainTextResponse)
async def receive_data_100(data_received: dict):
    return update_data(data_received)

# confirmed
@router.post('/update/200', response_class=PlainTextResponse)
async def receive_data_200(data_received: dict):
    return update_data(data_received)

# confirmed
@router.post('/update/300', response_class=PlainTextResponse)
async def receive_data_300(data_received: dict):
    return update_data(data_received)

# confirmed
@router.post('/update/400', response_class=PlainTextResponse)
async def receive_data_400(data_received: dict):
    return update_data(data_received)

# confirmed
@router.post('/update/500', response_class=PlainTextResponse)
async def receive_data_500(data_received: dict):
    return update_data(data_received)

# confirmed
@router.post('/update/600', response_class=PlainTextResponse)
async def receive_data_600(data_received: dict):
    return update_data(data_received)