from pydantic import BaseModel, validator


class Order(BaseModel):
    product_type: str
    product_name: str = None
    type: str = None

    @validator('product_type')
    def check_product_type(cls, value):
        if value not in ['physical_product', 'book', 'membership', 'video']:
            raise ValueError('Unsupported product type')
        return value
