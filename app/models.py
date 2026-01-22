from pydantic import BaseModel 

class User(BaseModel):
   user_id: int = 0
   username: str = ''
   email: str = ''