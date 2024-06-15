""" PyDantic models """

from pydantic import BaseModel


# Create your models here.
class TextModel(BaseModel):
    """Model for NLP"""

    text: str
