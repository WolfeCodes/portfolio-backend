from fastapi import APIRouter, Form

router = APIRouter(
    prefix="/contact",
    tags=["Contact"]
)

@router.post("/")
def submit_contact(name: str = Form(...),email: str = Form(...),message: str = Form(...)):
    print(f"Received contact form submission: Name: {name}, Email: {email}, Message: {message}")
    return {"status": "success", "message": "Contact form submitted successfully, Thank you for reaching out!"}