from pydantic import BaseModel

class CreateResponse(BaseModel):
   success:bool
   message:str