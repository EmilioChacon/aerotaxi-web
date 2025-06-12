from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

@app.get('/')
def root():
    """Root endpoint: returns a greeting message."""
    return {'message': 'Hello, Aerotaxi!'}

@app.get('/routes')
def get_routes():
    """Returns a list of available flight routes."""
    return [
        {"route_id": 1, "from": "Madrid", "to": "Barcelona", "duration": "1h 15m"},
        # ... other routes
    ]

@app.get('/booking')
def get_booking():
    """Returns booking placeholder info (for future implementation)."""
    return {"message": "Booking endpoint - coming soon!"}


# Pydantic model for booking input validation
class Booking(BaseModel):
    route_id: int
    from_: str = Field(..., alias="from")
    to: str
    passenger: str

    class Config:
        allow_population_by_field_name = True

@app.post('/booking')
def create_booking(booking: Booking):
    """Create a new flight booking."""
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
