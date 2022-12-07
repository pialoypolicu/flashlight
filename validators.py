from my_exceptions import ValidationError


async def is_valid(commands: dict) -> None:
    try:
        if not isinstance(commands["command"], str):
            raise ValidationError("command must be string")
        if not isinstance(commands["metadata"], str | None):
            raise ValidationError("metadata must be string or None")
    except KeyError as error:
        raise ValidationError(f"command and metadata are required {error}")