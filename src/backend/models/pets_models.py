from pydantic import BaseModel, Field
from typing import Optional


class Category(BaseModel):
    id: Optional[int] = Field(None, description="The ID of the category")
    name: Optional[str] = Field(None, description="The name of the category")


class Tag(BaseModel):
    id: Optional[int] = Field(None, description="The ID of the tag")
    name: Optional[str] = Field(None, description="The name of the tag")


class Pet(BaseModel):
    id: Optional[int] = Field(None, description="The ID of the pet")
    name: Optional[str] = Field(None, description="The name of the pet")
    category: Optional[Category] = Field(
        None, description="The category of the pet")
    photo_urls: Optional[list[str]] = Field(
        "", description="List of photo URLs for the pet")
    tags: Optional[list[Tag]] = Field(
        None, description="List of tags associated with the pet")
    status: str = Field(
        ...,
        description="The status of the pet",
        pattern="^(available|pending|sold)$"
    )
