import enum

from loguru import logger


@enum.unique
class ControlCommands(enum.Enum):
    off = 0
    on = 1
    color = 2

# А если мы добавим, скажем, еще 10 комманд - яркость, режим "стробоскопа"/обычный, 
# переключение на ультрафиолет/лампочку,и т.д. и т.п.
# будет также куча захардкоренных элементов, тем более "ифов"
# Исправьте на использование словаря, пожалуйста
def make_command(data) -> bool | None:
    command = data["command"].lower()
    if not hasattr(ControlCommands, command):
        return None
    if command == ControlCommands.on.name:
        logger.info("flashlight turn ON")
    elif command == ControlCommands.off.name:
        logger.info("flashlight turn OFF")
    elif command == ControlCommands.color.name:
        logger.info(f"change color {data['metadata']}")
    return True
