from marshmallow import Schema, fields


class ItemSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Str()


class StoreSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    items = fields.List(fields.Nested(ItemSchema()))

    

    
