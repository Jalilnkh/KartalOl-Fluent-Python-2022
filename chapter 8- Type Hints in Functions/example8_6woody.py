from typing import Any
from example8_4birds import *


woody = Bird()
alert(woody)
alert_duck(woody)
alert_bird(woody)

def double(x: Any) -> Any:
    return x * 2