from marshmallow import EXCLUDE, Schema, fields, validate, validates_schema, ValidationError

from constants.constants import ROLES

class AddUserSchema(Schema):
    first_name = fields.Str(
        required=True,
        validate=validate.Length(min=1),  
        error_messages={"required": "First name is required"}
    )

    last_name = fields.Str(
        required=True,
        validate=validate.Length(min=1),
        error_messages={"required": "Last name is required"}
    )

    email = fields.Email(
        required=True,
        error_messages={
            "required": "Email is required",
            "invalid": "Invalid email format"
        }
    )

    phone_number = fields.Str(allow_none=True)

    rola = fields.Str(
        required=True,
        validate=validate.OneOf(ROLES, error="Invalid role"),
        error_messages={"required": "Role is required"}
    )

    password = fields.Str(
        required=True,
        validate=validate.Length(min=6, error="Password must be at least 6 characters"),
        error_messages={"required": "Password is required"}
    )

    retype_password = fields.Str(
        required=True,
        error_messages={"required": "Please confirm password"}
    )

    biography = fields.Str(
        required=False,
        allow_none=True,
        validate=validate.Length(max=500)
    )

    @validates_schema
    def validate_custom(self, data, **kwargs):
        # Password match
        if data.get("password") != data.get("retype_password"):
            raise ValidationError({"retype_password": ["Passwords do not match"]})

        # Biography required if professor
        if data.get("rola") == "professor":
            bio = data.get("biography")
            if not bio:
                raise ValidationError({"biography": ["Biography is required for professors"]})
            if len(bio) > 500:
                raise ValidationError({"biography": ["Biography can be max 500 characters"]})
    class Meta:
        unknown = EXCLUDE