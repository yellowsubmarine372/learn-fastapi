from database import SessionLocal
from user.domain.repository.user_repo import IUserRepository
from user.domain.user import User as UserV0
from user.infra.db_models.user import User

class UserRepository(IUserRepository):
    def save(self, user: UserV0):
        new_user = User(
            id=user.id,
            email=user.profile.email,
            name=user.profile.name,
            password=user.password,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        
        with SessionLocal() as db:
            try:
                db = SessionLocal()
                db.add(new_user)
                db.commit()
            finally:
                db.close()
    
    def find_by_email(self, email: str) -> User:
        pass