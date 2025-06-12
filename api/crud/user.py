from sqlalchemy.orm import Session
from api.database.models.user import User
from api.database.schemas.user import UserCreate, UserUpdate, UserProfileUpdate
from datetime import datetime
from api.security import hash_password

# Create new user
def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        mob_number=user.mob_number,
        role=user.role,
        created_at=datetime.utcnow(),
        updated_at=None
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get all users
def get_all_users(db: Session):
    return db.query(User).all()

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get user by mobile number
def get_user_by_mobile(db: Session, mob_number: str):
    return db.query(User).filter(User.mob_number == mob_number).first()

# Get user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Update user details
def update_user(db: Session, user_id: int, updated_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    if updated_data.name is not None:
        user.name = updated_data.name

    if updated_data.email is not None:
        user.email = updated_data.email

    if updated_data.mob_number is not None:
        user.mob_number = updated_data.mob_number

    if updated_data.password:
        user.password = hash_password(updated_data.password)

    user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user

# Update user password (only new password)
def update_user_password(db: Session, user_id: int, new_password: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    user.password = hash_password(new_password)
    user.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(user)
    return user

# Delete user by ID
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    db.delete(user)
    db.commit()
    return user



def update_user_profile(db: Session, user_id: int, updated_data: UserProfileUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    # Only update fields if they are explicitly sent
    if updated_data.name is not None:
        user.name = updated_data.name

    if updated_data.email is not None:
        user.email = updated_data.email

    if updated_data.mob_number is not None:
        user.mob_number = updated_data.mob_number

    user.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(user)
    return user
