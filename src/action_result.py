

class ActionResult:

    def __init__(self,text:str,point:int) -> None:
        self._text = text
        self.point = point

    def __str__(self) -> str:
        return self._text
    