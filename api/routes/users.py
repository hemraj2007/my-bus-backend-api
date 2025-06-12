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
# Update Profile by Admin (based on user_id)
@router.put("/update_profile/{user_id}", response_model=UserResponse)
def update_user_profile_by_id(
    user_id: int,
    updated_data: UserProfileUpdate,
    db: Session = Depends(get_db)
):
    """
    Admin can update any user's profile using user_id
    """
    user = user_crud.update_user_profile(db, user_id, updated_data)

    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    return UserResponse.from_orm(user)




@router.get("/users", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = user_crud.get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found.")
    return users
