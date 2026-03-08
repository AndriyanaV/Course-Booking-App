from marshmallow import EXCLUDE, Schema, fields, pre_load, validate, validates, validates_schema, ValidationError
from constants.constants import COUNTRY_CODES, ROLES
import re


class UpdateUserProfileSchema(Schema):
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

    phone_number = fields.Str(
        required=False,
        allow_none=True,
    )

    biography = fields.Str(
        required=False,
        allow_none=True,
        validate=validate.Length(max=500)
    )

    # Validator za telefon
    @validates("phone_number")
    def validate_phone_number(self, value, **kwargs):
        if not value:
            return  # prazno je ok

        country = next((c for c in COUNTRY_CODES if value.startswith(c["code"])), None)
        if not country:
            raise ValidationError("Phone number prefix not recognized")
        if not re.fullmatch(country["regex"], value):
            raise ValidationError(f"Invalid phone number format for {country['label']}")

    # Validator biografije za profesora
    @validates_schema
    def validate_biography_for_professor(self, data, **kwargs):
        role = None
        if self.context.get("current_user"):
            role = getattr(self.context.get("current_user"), "rola", None)

        biography = data.get("biography")
        if role == "professor" and biography is not None:
            if biography.strip() == "":
                raise ValidationError({"biography": "Biography cannot be empty for professor"})

    # Pretvaranje praznog stringa u None za opcionalna polja
    @pre_load
    def empty_str_to_none(self, data, **kwargs):
        optional_fields = ["phone_number", "biography"]
        for field in optional_fields:
            if field in data and data[field] == "":
                data[field] = None
        return data

    class Meta:
        unknown = EXCLUDE