from marshmallow import Schema, fields



class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    location = fields.Str(required=True)
    name = fields.Str(required=True)


class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True) 
    price = fields.Float(required=True)

class ProductSchema(PlainProductSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class StoreSchema(PlainStoreSchema):
    product = fields.Nested(PlainProductSchema(), dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class ProductUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

class PlainPurchaseHistorySchema(Schema):
    date = fields.Date()

class PurchaseHistorySchema(Schema):
    user_id = fields.Int(required=True)
    item_id = fields.Int(required=True)
    item_id = fields.Str(required=True)
    store_id = fields.Int(required=True)











