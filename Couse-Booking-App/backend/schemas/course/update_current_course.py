from datetime import date, datetime
from marshmallow import Schema, fields, validate, ValidationError, validates_schema
from constants.constants import LEVELS

class UpdateCurrentCourseSchema(Schema):
    user_id = fields.Int(
        required=False,
        validate=validate.Range(min=1, error="Professor ID must be a positive integer"),
        error_messages={"invalid": "Professor ID must be an integer"}
    )
    price = fields.Float(
        required=False,
        validate=validate.Range(min=0, error="Price must be positive"),
        error_messages={"invalid": "Price must be a number"}
    )
    max_members = fields.Int(
        required=False,
        validate=validate.Range(min=1, error="Max members must be positive"),
        error_messages={"invalid": "Max members must be an integer"}
    )
    start_at = fields.DateTime(
        required=False,
        error_messages={"invalid": "Start date must be a valid datetime"}
    )
    end_at = fields.Date(
        required=False,
        error_messages={"invalid": "End date must be a valid date"}
    )
    location = fields.Str(
        required=False,
        validate=[
            validate.Length(min=1, error="Location cannot be empty"),
            validate.Regexp(r"\S", error="Location cannot be empty or whitespace only")
        ]
    )
    lessons = fields.Int(
        required=False,
        validate=validate.Range(min=1, error="Number of lessons must be positive"),
        error_messages={"invalid": "Number of lessons must be an integer"}
    )
    level = fields.Str(
        required=False,
        validate=[
            validate.OneOf(LEVELS, error="Please choose a valid level"),
            validate.Regexp(r"\S", error="Level cannot be empty or whitespace only")
        ]
    )

    @validates_schema
    def validate_dates(self, data, **kwargs):
        # validacija samo ako oba polja postoje
        start = data.get("start_at")
        end = data.get("end_at")
        if start and end:
            if isinstance(start, date) and not isinstance(start, datetime):
                start = datetime.combine(start, datetime.min.time())
            if isinstance(end, date) and not isinstance(end, datetime):
                end = datetime.combine(end, datetime.min.time())

            if end < start:
                raise ValidationError(
                    {"end_at": ["End date cannot be before start date"]}
                )