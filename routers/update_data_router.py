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


# update alert
@router.post('/alert/7/1', response_class=PlainTextResponse)
async def alert_7_1(data_received: dict):
    return update_alert(data_received)

@router.post('/alert/7/2', response_class=PlainTextResponse)
async def alert_7_2(data_received: dict):
    return update_alert(data_received)

@router.post('/alert/7/3', response_class=PlainTextResponse)
async def alert_7_3(data_received: dict):
    return update_alert(data_received)

@router.post('/alert/7/4', response_class=PlainTextResponse)
async def alert_7_4(data_received: dict):
    location_id = 7
    return update_alert(data_received, location_id)

@router.post('/alert/8/1', response_class=PlainTextResponse)
async def alert_8_1(data_received: dict):
    return update_alert(data_received)

@router.post('/alert/10/2', response_class=PlainTextResponse)
async def alert_10_2(data_received: dict):
    return update_alert(data_received)

@router.post('/alert/11/2', response_class=PlainTextResponse)
async def alert_11_2(data_received: dict):
    return update_alert(data_received)