from marshmallow import Schema, fields, validate

class AddCourseSchema(Schema):
    name = fields.Str(
        required=True,
        validate=validate.Length(min=5, max=100),
        error_messages={"required": "Course name is required!"}
    )
    language = fields.Str(
        required=True,
        validate=validate.Length(min=5),
        error_messages={"required": "Language is required!"}
    )