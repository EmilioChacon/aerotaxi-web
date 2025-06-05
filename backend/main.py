from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Hello, Aerotaxi!'}

@app.get('/booking')
def get_booking():
    return {"message": "Booking endpoint - coming soon!."}