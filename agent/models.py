from sqlmodel import SQLModel, Field
from enum import Enum

class RoleMessage(str,Enum):
    USER = "user"
    MODEL = "model"
    SYSTEM = "system"


class ConversationMessage(SQLModel, table=True):
    id: int | None =Field(default=None, primary_key=True)
    role: RoleMessage = RoleMessage.USER
    content: str

class ToolExecutionLog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tool_name: str
    arguments: str
    result: str
    is_sucess: bool
    timestamp: str
