from tkinter import Canvas, Misc, _Color, _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, _XYScrollCommand
from typing import Any, Literal
from TkCanvasUI2.Collider import Polygon


class BaseWidget:

    def __init__(self) -> None:
        self.collisions: list[Polygon] = []

    def redraw(self): ...

    def is_collision(self, coord): ...

    def button_1_event(self, event): ...


class BaseCanvasUI(Canvas):
    def __init__(
        self,
        master: Misc | None = ...,
        cnf: dict[str, Any] | None = ...,
        *,
        background: _Color = ...,
        bd: _ScreenUnits = ...,
        bg: _Color = ...,
        border: _ScreenUnits = ...,
        borderwidth: _ScreenUnits = ...,
        closeenough: float = ...,
        confine: bool = ...,
        cursor: _Cursor = ...,
        # canvas manual page has a section named COORDINATES, and the first
        # part of it describes _ScreenUnits.
        height: _ScreenUnits = ...,
        highlightbackground: _Color = ...,
        highlightcolor: _Color = ...,
        highlightthickness: _ScreenUnits = ...,
        insertbackground: _Color = ...,
        insertborderwidth: _ScreenUnits = ...,
        insertofftime: int = ...,
        insertontime: int = ...,
        insertwidth: _ScreenUnits = ...,
        name: str = ...,
        offset: Any = ...,  # undocumented
        relief: _Relief = ...,
        # Setting scrollregion to None doesn't reset it back to empty,
        # but setting it to () does.
        scrollregion: tuple[_ScreenUnits, _ScreenUnits, _ScreenUnits, _ScreenUnits] | tuple[()] = ...,
        selectbackground: _Color = ...,
        selectborderwidth: _ScreenUnits = ...,
        selectforeground: _Color = ...,
        # man page says that state can be 'hidden', but it can't
        state: Literal["normal", "disabled"] = ...,
        takefocus: _TakeFocusValue = ...,
        width: _ScreenUnits = ...,
        xscrollcommand: _XYScrollCommand = ...,
        xscrollincrement: _ScreenUnits = ...,
        yscrollcommand: _XYScrollCommand = ...,
        yscrollincrement: _ScreenUnits = ...,
    ) -> None:
        self.widgets: list[BaseWidget] = []

    def draw(self) -> None: ...

    def button_1_event(self, event: Any) -> None: ...

    def collision(self, param): ...

    def add(self, widget: BaseWidget) -> None: ...