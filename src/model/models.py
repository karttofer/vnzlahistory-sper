# dependencies
from pydantic import BaseModel, Field

class Img(BaseModel):
    img: str = Field(description="Place to set the img url")