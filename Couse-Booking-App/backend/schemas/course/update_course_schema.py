from marshmallow import Schema, fields, validate

class UpdateCourseSchema(Schema):
    name = fields.Str(
        required=False,  # not required
        validate=[
            validate.Length(
                min=5, max=30,
                error="Course name must be between 5 and 30 characters"
            ),
            validate.Regexp(r"\S", error="Course name cannot be empty")
        ]
    )
    language = fields.Str(
        required=False,  # not required
        validate=[
            validate.Length(
                min=5, max=20,
                error="Course language must be between 5 and 20 characters"
            ),
            validate.Regexp(r"\S", error="Language cannot be empty")
        ]
    )
    