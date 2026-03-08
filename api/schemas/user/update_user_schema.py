from marshmallow import Schema, ValidationError, fields, pre_load, validate, EXCLUDE, validates, validates_schema
from constants.constants import COUNTRY_CODES, ROLES
import re

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

    # Phone number validator with COUNTRY_CODES
    @validates("phone_number")
    def validate_phone_number(self, value, **kwargs):
        if not value:
            return  # prazno je ok

        # pronalazimo odgovarajući country code
        country = next((c for c in COUNTRY_CODES if value.startswith(c["code"])), None)
        if not country:
            raise ValidationError("Phone number prefix not recognized")

        # regex validacija
        if not re.fullmatch(country["regex"], value):
            raise ValidationError(f"Invalid phone number format for {country['label']}")

    @validates_schema
    def validate_biography_for_professor(self, data, **kwargs):
        role = data.get("rola")
        if not role and self.context.get("current_user"):
            role = self.context.get("current_user").rola

        biography = data.get("biography")
        if role == "professor" and biography is not None:
            if biography.strip() == "":
                raise ValidationError(
                    {"biography": "Biography cannot be empty for professor"}
                )
    @pre_load
    def empty_str_to_none(self, data, **kwargs):
        optional_fields = ["phone_number", "biography"]
        for field in optional_fields:
            if field in data and data[field] == "":
                data[field] = None
        return data

    class Meta:
        unknown = EXCLUDE