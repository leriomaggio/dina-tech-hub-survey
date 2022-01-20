from typing import Union, Callable
import matplotlib.pyplot as plt
import pandas as pd

# Chart Data Folder
from os import path
import os
from pathlib import Path

CHART_FOLDER = Path(path.abspath("./charts"))
if not path.exists(CHART_FOLDER):
    os.makedirs(CHART_FOLDER, exist_ok=True)

COLOR_MAP = plt.get_cmap("Dark2")


def bar_plot(
    df: pd.DataFrame,
    columns: list[str],
    title: str,
    filename: Union[Path, str],
    unstack_ord: tuple[int] = None,
    selection: pd.DataFrame = None,
    aggregate: str = None,
    groupby_cols: list[str] = None,
    sorted: str = "index",
    legend: bool = None,
    ticks_rotation=0,
    figsize: tuple[int] = (12, 6),
    width: float = 0.5,
    alpha: float = 0.5,
    horizontal: bool = False,
    colors: list[tuple[float]] = COLOR_MAP.colors,
) -> None:
    if columns is None or not len(columns):
        raise ValueError("Selection Columns MUST be specified!")

    if aggregate is None:
        aggregate = "value_counts"

    if not sorted in ("index", "values", None):
        raise ValueError(
            "Invalid value for sorted parameter. Accepted values are 'index', 'values', or 'None'"
        )

    if len(columns) == 1:
        columns = columns[0]
    else:
        columns = list(columns)

    if legend is None:  # default
        legend = (
            True  # will be automatically inferred based on how many cols are selected
        )

    chart_filepath = CHART_FOLDER / filename
    if not filename.endswith(".pdf"):
        filename += ".pdf"

    if selection is not None:
        df_chart = df[selection][columns]
    else:
        df_chart = df[columns]

    if groupby_cols:
        if len(groupby_cols) == 1:
            groupby_cols = groupby_cols[0]
        else:
            groupby_cols = list(groupby_cols)
        df_chart = df_chart.groupby(groupby_cols)

    agg = getattr(df_chart, aggregate)
    df_chart = agg()
    if sorted is not None:
        df_chart = (
            df_chart.sort_index() if sorted == "index" else df_chart.sort_values()
        )

    if len(columns) > 1 and unstack_ord is not None:
        for idx in unstack_ord:
            df_chart = df_chart.unstack(idx)
    if not horizontal:
        ax = df_chart.plot.bar(
            figsize=figsize,
            width=width,
            color=colors,
            alpha=alpha,
            title=title,
            rot=ticks_rotation,
        )
    else:
        ax = df_chart.plot.barh(
            figsize=figsize,
            width=width,
            color=colors,
            alpha=alpha,
            title=title,
            rot=ticks_rotation,
        )

    if (
        legend and len(columns) > 1
    ):  # adding legend only if more than one column is being selected
        if not horizontal:
            plt.legend(ncol=3, loc=(0, 1.1))
        else:
            plt.legend(loc=(1, 0))
    for container in ax.containers:
        labels = [
            str(int(value)) if value > 0 else "" for value in container.datavalues
        ]
        ax.bar_label(container, labels=labels)
        # ax.bar_label(container)
    # print(df_chart.head().index.values.tolist())
    # ax.set_xticklabels([textwrap.fill(" ".join(i) if hasattr(i, "__len__") else i, 15) for i in df_chart.head().index.values.tolist()])

    plt.savefig(
        chart_filepath, dpi=1200, format="pdf", pad_inches=0.5, bbox_inches="tight"
    )
