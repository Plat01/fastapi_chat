import uuid
from sqlalchemy import MetaData, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import PhoneNumberType, EmailType

from app.database import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, UUID_ID, GUID


metadata = MetaData()


class User(SQLAlchemyBaseUserTableUUID, Base):

    __tablename__ = "user"

    id: Mapped[UUID_ID] = mapped_column(
        GUID, primary_key=True, default=uuid.uuid4
    )
    user_name: Mapped[str] = mapped_column(
        String(length=255), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        EmailType(), unique=True, index=True, nullable=False
    )
    phone_number: Mapped[str] = mapped_column(
        PhoneNumberType(region="RU"), unique=True, nullable=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )


if __name__ == '__main__':
    print(User.__table__)
    print(User.__table__.columns)

    from app.database import engine

    async def create_db_and_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
