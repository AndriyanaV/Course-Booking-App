from datetime import date, datetime
from marshmallow import Schema, fields, validate, ValidationError, validates_schema

from constants.constants import LEVELS

class AddCurrentCourseSchema(Schema):
    course_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Course ID must be a positive integer"),
        error_messages={"required": "Course ID is required", "invalid": "Course ID must be an integer"}
    )
    user_id = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Professor ID must be a positive integer"),
        error_messages={"required": "Professor data is required", "invalid": "Professor ID must be an integer"}
    )
    price = fields.Float(
        required=True,
        validate=validate.Range(min=0, error="Price must be positive"),
        error_messages={"required": "Price is required", "invalid": "Price must be a number"}
    )
    max_members = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Max members must be positive"),
        error_messages={"required": "Max members is required", "invalid": "Max members must be an integer"}
    )
    start_at = fields.DateTime(
        required=True,
        error_messages={
            "required": "Start date is required",
            "invalid": "Start date must be a valid datetime"
        })
    end_at = fields.Date(
        required=True,
        error_messages={"required": "End date is required", "invalid": "End date must be a valid date"}
    )
    location = fields.Str(
        required=True,
        validate=[
        validate.Length(min=1, error="Location cannot be empty"),
        validate.Regexp(r"\S", error="Location cannot be empty or whitespace only")
        ],
        error_messages={"required": "Location is required"}
    )
    lessons = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Number of lessons must be positive"),
        error_messages={"required": "Number of lessons is required", "invalid": "Number of lessons must be an integer"}
    )
    level = fields.Str(
        required=True,
        validate=[
        validate.OneOf(LEVELS, error="Please choose a valid level"),
        validate.Regexp(r"\S", error="Level cannot be empty or whitespace only")
        ],
        error_messages={"required": "Level is required"}
    )
    

    @validates_schema
    def validate_dates(self, data, **kwargs):
        if "start_at" in data and "end_at" in data:
            start = data["start_at"]
            end = data["end_at"]

        # Ako su tipa date, pretvori u datetime radi poređenja
        if isinstance(start, date) and not isinstance(start, datetime):
            start = datetime.combine(start, datetime.min.time())
        if isinstance(end, date) and not isinstance(end, datetime):
            end = datetime.combine(end, datetime.min.time())

        if end < start:
            raise ValidationError(
                {"end_at": ["End date cannot be before start date"]}
            )