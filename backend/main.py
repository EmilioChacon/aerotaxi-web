# FastAPI application for Aerotaxi service
# This application provides endpoints for booking flights and retrieving routes.
from fastapi import FastAPI
from pydantic import BaseModel #Import BaseModel for data validation 

app = FastAPI() # Initialize FastAPI application

# Root endpoint
@app.get('/') 
def root():
    return {'message': 'Hello, Aerotaxi!'}

# Endpoint to get booking information
@app.get('/booking')
def get_booking():
    return {"message": "Booking endpoint - coming soon!."}

# Endpoint to get available routes
@app.get('/routes')
def get_routes():
    return [
        {"route_id": 1, "from": "Madrid", "to": "Barcelona", "duration": "1h 15m"},
        {"route_id": 2, "from": "Barcelona", "to": "Valencia", "duration": "1h 30m"},
        {"route_id": 3, "from": "Valencia", "to": "Seville", "duration": "1h 45m"},
        {"route_id": 4, "from": "Seville", "to": "Madrid", "duration": "1h 50m"},
        {"route_id": 5, "from": "Madrid", "to": "Bilbao", "duration": "1h 20m"},
        {"route_id": 6, "from": "Bilbao", "to": "San Sebastian", "duration": "1h 10m"},
        {"route_id": 7, "from": "San Sebastian", "to": "Barcelona", "duration": "1h 40m"},
        {"route_id": 8, "from": "Barcelona", "to": "Madrid", "duration": "1h 25m"},
        {"route_id": 9, "from": "Madrid", "to": "Malaga", "duration": "1h 30m"},
        {"route_id": 10, "from": "Malaga", "to": "Granada", "duration": "1h 20m"},
        {"route_id": 11, "from": "Granada", "to": "Seville", "duration": "1h 15m"},
        {"route_id": 12, "from": "Seville", "to": "Malaga", "duration": "1h 10m"},
        {"route_id": 13, "from": "Malaga", "to": "Bilbao", "duration": "1h 50m"},
        {"route_id": 14, "from": "Bilbao", "to": "Madrid", "duration": "1h 30m"},
        {"route_id": 15, "from": "Madrid", "to": "Valencia", "duration": "1h 20m"}
    ]

# Define the Booking model for flight booking
class Booking(BaseModel):
    route_id: int
    from_: str
    to: str
    passenger: str

# Endpoint to book a flight
@app.post('/book')
def book_flight(booking: Booking):
    return {
        "status": "success",
        "message": "Aerotaxi booked successfully!",
        "booking_details": {
            "route_id": booking.route_id,
            "from": booking.from_,
            "to": booking.to,
            "passenger": booking.passenger
        }
    }