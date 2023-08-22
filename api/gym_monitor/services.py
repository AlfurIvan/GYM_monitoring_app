import dataclasses
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import News, TrainingProgram


@dataclasses.dataclass
class NewsDataClass:
    id: int
    title: str
    body: str
    pub_date: datetime
    image: str

    @classmethod
    def from_instance(cls, news_model: "News") -> "NewsDataClass":
        return cls(
            id=news_model.id,
            title=news_model.title,
            body=news_model.body,
            pub_date=news_model.pub_date,
            image=news_model.image,
        )


@dataclasses.dataclass
class TrainingProgramDataClass:
    id: int
    title: str
    body: str
    tags: str

    @classmethod
    def from_instance(cls, prog_model: "TrainingProgram") -> "TrainingProgramDataClass":
        return cls(
            id=prog_model.id,
            title=prog_model.title,
            body=prog_model.body,
            tags=prog_model.tags,
        )
