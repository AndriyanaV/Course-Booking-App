from marshmallow import EXCLUDE, Schema, fields, pre_load, validate, validates, validates_schema, ValidationError
from constants.constants import COUNTRY_CODES, ROLES
import re

class AddUserSchema(Schema):
    first_name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, error="First name is required"),
            validate.Regexp(r"\S", error="First name cannot be whitespace only")
        ]
    )

    last_name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, error="Last name is required"),
            validate.Regexp(r"\S", error="Last name cannot be whitespace only")
        ]
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

    @validates("phone_number")
    def validate_phone_number(self, value, **kwargs):
        if not value:
            return  # prazno je ok, upisuje se NULL u DB

        # pronalazimo odgovarajući country code
        country = next((c for c in COUNTRY_CODES if value.startswith(c["code"])), None)
        if not country:
            raise ValidationError("Phone number prefix not recognized")

        # regex validacija
        if not re.fullmatch(country["regex"], value):
            raise ValidationError(f"Invalid phone number format for {country['label']}")

    @validates_schema
    def validate_custom(self, data, **kwargs):
        # Password match
        if data.get("password") != data.get("retype_password"):
            raise ValidationError({"retype_password": ["Passwords do not match"]})

        # Biography required if professor
        if data.get("rola") == "professor":
            bio = data.get("biography")
            if not bio or not bio.strip():
                raise ValidationError({"biography": ["Biography is required for professors"]})
            if len(bio) > 500:
                raise ValidationError({"biography": ["Biography can be max 500 characters"]})

    # Pretvaramo prazne stringove u None
    @pre_load
    def empty_str_to_none(self, data, **kwargs):
        optional_fields = ["phone_number", "biography"]
        for field in optional_fields:
            if field in data and data[field] == "":
                data[field] = None
        return data

    class Meta:
        unknown = EXCLUDE