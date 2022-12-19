from my_exceptions import ValidationError


# Такие проверки, как и перебор ифами в клиенте - делают поддержку решения болезненным
# 7. Реализация фонаря позволяет легко добавлять любые новые команды
# привяжите, пожалуйста, проверки к словарю, как единой точке всех изменений в системе
def is_valid(commands: dict) -> None:
    if not isinstance(commands.get("command"), str):
        raise ValidationError("command is required and must be a string")
    try:
        if not isinstance(commands["metadata"], str | None):
            raise ValidationError("metadata must be string or None")
    except KeyError as error:
        raise ValidationError(f"command and metadata are required {error}")
