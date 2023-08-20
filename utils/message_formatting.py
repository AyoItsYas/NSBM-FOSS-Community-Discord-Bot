from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Iterable, Union


def align_to_columns(
    data: Iterable[Iterable[str]],
    *,
    column_sep: Union[Iterable[str], str] = " ",
) -> str:
    """Align strings into aligned columns.

    Args:
        data (Iterable[Iterable[str]]): Matrix of strings to align.
        column_sep (Union[Iterable[str], str], optional): Column seperator. Can either be an Iterable that specifies a seperator between each column or a string that is used to seperate each column. Defaults to None.

    Raises:
        ValueError: Raises ValueError if column_sep is an Iterable and the length of the Iterable is not equal to the number of columns.

    Returns:
        str: Returns a string with the aligned columns.
    """
    column_max_widths = [max(map(len, column)) for column in zip(*data)]

    if column_sep is not None:
        if isinstance(column_sep, str):
            column_sep = [column_sep] * (len(column_max_widths) - 1)
        elif len(column_sep) != len(column_max_widths) - 1:
            raise ValueError(
                f"must provide {len(column_max_widths) - 1} column separators for {len(column_max_widths)} columns"
            )

    lines = []
    for row in data:
        line = ""
        for i, (column, width) in enumerate(zip(row, column_max_widths)):
            line += column.ljust(width)
            if column_sep and i != len(row) - 1:
                line += column_sep[i]
        lines.append(line)

    return "\n".join(lines)
