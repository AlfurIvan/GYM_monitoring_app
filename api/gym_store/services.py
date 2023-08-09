import dataclasses
import datetime
from typing import TYPE_CHECKING

from user import services as user_services


if TYPE_CHECKING:
    from .models import Pass, Product


@dataclasses.dataclass
class PassDataClass:
    id: int
    price: int
    month_to_expire: int
    date_released: datetime.datetime = None
    user: user_services.UserDataClass = None
    staff_who_released: user_services.UserDataClass = None

    @classmethod
    def from_instance(cls, pass_model: "Pass") -> "PassDataClass":
        return cls(
            id=pass_model.id,
            price=pass_model.price,
            month_to_expire=pass_model.month_to_expire,
            date_released=pass_model.date_released,
            user=pass_model.user,
            staff_who_released=pass_model.staff_who_released,
        )


@dataclasses.dataclass
class ProductDataClass:
    id: int
    title: str
    description: str
    manufacturer: str
    price: int
    amount: int

    @classmethod
    def from_instance(cls, prod_model: "Product") -> "ProductDataClass":
        return cls(
            id=prod_model.id,
            title=prod_model.title,
            description=prod_model.description,
            manufacturer=prod_model.manufacturer,
            price=prod_model.price,
            amount=prod_model.amount,
        )
