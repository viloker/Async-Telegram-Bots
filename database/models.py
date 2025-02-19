from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from database.db_config import Base
from typing import List


class Chat(Base):

    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(primary_key=True)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    name: Mapped[str] = mapped_column(nullable=True)


    messages: Mapped[List["Message"]] = relationship(
        back_populates="chat", lazy="select", cascade="all, delete-orphan"
    )

    def __str__(self):
        return f"<Chat(chat_id={self.id}, chat.name={self.name}, prompt={self.prompt[:20]}...)>"


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"), nullable=False,
                                         index=True)
    user_id: Mapped[int] = mapped_column(nullable=False, index=True)
    user_name: Mapped[str] = mapped_column(nullable=True)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    time: Mapped[datetime] = mapped_column(default=datetime.now, index=True)

    chat: Mapped["Chat"] = relationship(back_populates="messages", lazy="joined")

    def __str__(self):
        return f"<Message(id={self.id}, chat_id={self.chat_id}, text={self.text[:20]}...)>"


class Bot(Base):

    __tablename__ = 'bots'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(Text, nullable=False)
    signal: Mapped[bool] = mapped_column(default=False)
    main: Mapped[bool] = mapped_column(default=False)

    def __str__(self):
        return f"<Bot(name={self.name}, signal={self.signal})>"
