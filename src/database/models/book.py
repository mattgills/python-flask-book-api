from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Decimal
import enum

Base = declarative_base()

class MediaEnum(enum.Enum):
    PRINT = 'print'
    EBOOK = 'ebook'
    AUDIO = 'audio'

class Book(Base):
    __tablename__ = 'book'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String, nullable=False)
    authors = Column(String, nullable=False)
    isbn = Column(String, nullable=True)
    isbn13 = Column(String, nullable=True)
    publisher = Column(String, nullable=True)
    edition = Column(String, nullable=True)
    length = Column(Decimal, nullable=False)
    media = Column(MediaEnum, nullable=False, default=MediaEnum.PRINT)