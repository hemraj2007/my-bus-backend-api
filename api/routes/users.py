from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.database.schemas.user import UserResponse, PasswordUpdate, UserProfileUpdate
from api.token import get_current_user
from api.database.connection import get_db
from api.database import models  # Importing models
from api.crud import user as user_crud  # Importing user CRUD functions

router = APIRouter()

# Profile fetch
@router.get("/profile", response_model=UserResponse)
def get_profile(current_user: UserResponse = Depends(get_current_user)):
    return current_user

# Password Update (without current password)
@router.put("/update_password")
def update_password(
    data: PasswordUpdate,
    current_user: UserResponse = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify new password == confirm password
    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="New password and confirm password do not match.")

    # Update password
    updated_user = user_crud.update_user_password(db, current_user.id, data.new_password)
    if not updated_user:
        raise HTTPException(status_code=500, detail="Something went wrong while updating password.")

    return {"message": "Password updated successfully."}

# Update Profile
@router.put("/update_profile", response_model=UserResponse)
def update_profile(
    updated_data: UserProfileUpdate,  # Accepting the data from the user
    current_user: UserResponse = Depends(get_current_user),  # Getting the currently authenticated user, using UserResponse here
    db: Session = Depends(get_db)  # Dependency injection for DB session
):
    """
    Endpoint for updating the profile of the currently authenticated user.
    """
    # Call the CRUD function to update the user's profile in the database
    user = user_crud.update_user_profile(db, current_user.id, updated_data)

    # If no user is found, raise HTTP 404 error
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    # Return the updated user profile
    return UserResponse.from_orm(user)


@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = user_crud.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found.")
    return users
