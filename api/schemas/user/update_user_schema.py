from marshmallow import Schema, ValidationError, fields, validate, EXCLUDE, validates_schema
from constants.constants import ROLES

class UpdateUserSchema(Schema):

    first_name = fields.Str(
        required=False,
        validate=[
            validate.Length(min=1, error="First name cannot be empty"),
            validate.Regexp(r"\S", error="First name cannot be whitespace only")
        ]
    )

    last_name = fields.Str(
        required=False,
        validate=[
            validate.Length(min=1, error="Last name cannot be empty"),
            validate.Regexp(r"\S", error="Last name cannot be whitespace only")
        ]
    )

    email = fields.Email(
        required=False,
        error_messages={
            "invalid": "Invalid email format"
        }
    )

    phone_number = fields.Str(
        required=False,
        allow_none=True,
        validate=validate.Regexp(
            r"^\+?[0-9\s\-()]{6,20}$",
            error="Invalid phone number format"
        )
    )

    rola = fields.Str(
        required=False,
        validate=validate.OneOf(ROLES, error="Invalid role")
    )

    biography = fields.Str(
        required=False,
        allow_none=True,
        validate=validate.Length(max=500)
    )

    @validates_schema
    def validate_biography_for_professor(self, data, **kwargs):
        role = data.get("rola")

        if not role:
            role = self.context.get("current_user").rola

        biography = data.get("biography")

        if role == "professor" and biography is not None:
            if biography.strip() == "":
                raise ValidationError(
                {"biography": "Biography cannot be empty for professor"}
                )
    class Meta:
        unknown = EXCLUDE