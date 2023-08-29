import dataclasses
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import TrainingProgram


@dataclasses.dataclass
class TrainingProgramDataClass:
    id: int
    title: str
    body: str
    tags: str
    image:str

    @classmethod
    def from_instance(cls, prog_model: "TrainingProgram") -> "TrainingProgramDataClass":
        return cls(
            id=prog_model.id,
            title=prog_model.title,
            body=prog_model.body,
            tags=prog_model.tags,
            image=prog_model.image,
        )
