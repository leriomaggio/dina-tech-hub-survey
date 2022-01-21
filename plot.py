import os
import matplotlib.pyplot as plt
import pandas as pd

from typing import Union
from itertools import filterfalse

# Chart Data Folder
from pathlib import Path

CHART_FOLDER = Path(os.path.join(os.path.abspath(os.path.dirname(__file__)), "charts"))
if not os.path.exists(CHART_FOLDER):
    os.makedirs(CHART_FOLDER, exist_ok=True)

COLOR_MAP = plt.get_cmap("Set2")


def bar_plot(
    df: pd.DataFrame,
    columns: list[str],
    title: str,
    filename: Union[Path, str] = None,
    unstack_ord: tuple[int] = None,
    selection: pd.DataFrame = None,
    aggregate: str = "value_counts",
    groupby_cols: list[str] = None,
    sorted: str = "index",
    cap_threshold: int = 0,
    legend: bool = True,
    ticks_rotation=0,
    figsize: tuple[int] = (12, 6),
    width: float = 0.5,
    alpha: float = 0.5,
    horizontal: bool = False,
    colors: list[tuple[float]] = COLOR_MAP.colors,
) -> None:
    """
    Utility function to visualise data (descriptive) statistics as a bar plot.

    The bar plot is rather customisable in both data selection, and figure attributes
    (e.g. figsize, horizontal or vertical bars, legend).
    Option to save the bar plot in a PDF file, instead of just visualising it.

    Parameters
    ----------
    df : pd.DataFrame
        Data Frame containing the reference data
    columns : list[str]
        List of columns in the Data Frame to select from the original data frame.
        If None or empty list will be provided, all data frame columns will be considered instead, although quite unlikely.
        Similarly, if any column name will not be found in the dataframe, an exception will be raised.
    title : str
        Title of the plot
    filename : Union[Path, str], optional
        Name of the PDF file to save containing the whole barplot figure.
    unstack_ord : tuple[int], optional
        Tuple of indices of the corresponding index to repeatedly unstack from the resulting statistics-dataframe, if any.
        By default is None, meaning no `unstack` operation will be applied nor tempted to the resulting dataframe.
    selection : pd.DataFrame, optional
        Filter to apply on data prior generating the plot, by default None.
        This filter should be specified in any form compliant to pandas data selection mechanism.
    aggregate : str, optional
        Name of the pandas function to apply to gather the statistics from the data, by default "value_counts"
    groupby_cols : list[str], optional
        Columns in the dataframe to be used as mapper for a groupby operation (prior aggregating the statistics for the plot).
        By default None which means that no groupby operation will be applied on the data.
        If any groupby column won't be found in the input dataframe, an exception will be raised.
    sorted : str, optional
        Determines whether data should be sorted. Accepted sorting criteria are "index" (default), "value", or None (No sorting).
    cap_threshold: int, optional
        If provided, any value (or count) below the threshold will be dropped from the plot. Zero by default
    legend : bool, optional
        Optional parameter to control whether a legend should be added to the barplot. If True (default), a legend will be added
        only if more than one column (series) of data was selected. No legend will be added otherwise. Conversely, if this parameter
        is passed to as False, no legend will be added, regardless.
    ticks_rotation : int, optional
        Parameter to control the (degrees of) rotation of ticks on the x-axis, by default 0
    figsize : tuple[int], optional
        Size of the generated Matplotlib figure, by default (12, 6)
    width : float, optional
        Width of the bars in the bar plot, by default 0.5
    alpha : float, optional
        Alpha value of colours of each series, by default 0.5
    horizontal : bool, optional
        Flag controlling whether bar plot should be horizontal or vertical. By default False, which will generate a bar plot.
    colors : list[tuple[float]], optional
        List of colours to apply to each series, by default the "Dark2" Matplotlib Colormap will be used.
        Please note that the number of provided colours must be greater or equal to the number of data series in the plot.

    Raises
    ------
    ValueError
        If coloumns or groupby_cols specified are not found in the reference dataframe
    ValueError
        If the value of sorted parameter is not one of "index", "value", None.
    """
    if columns is None or not len(columns):
        columns = df.columns

    if any([col not in df.columns for col in columns]):
        not_found = list(filterfalse(lambda c: c in df.columns, columns))
        raise ValueError(
            f"Invalid specified columns. Column{'s' if len(not_found) > 1 else ''} {not_found} cannot be found in input dataframe."
        )

    if groupby_cols and any([col not in df.columns for col in groupby_cols]):
        not_found = list(filterfalse(lambda c: c in df.columns, groupby_cols))
        raise ValueError(
            f"Invalid specified GroupBy columns: column{'s' if len(not_found) > 1 else ''} {not_found} cannot be found in input dataframe."
        )

    if not aggregate:
        aggregate = "value_counts"

    if not sorted in ("index", "values", None):
        raise ValueError(
            "Invalid value for sorted parameter. Accepted values are 'index', 'values', or 'None'"
        )

    if len(columns) == 1:
        columns = columns[0]
    else:
        columns = list(columns)

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

    if cap_threshold:
        df_chart = df_chart[df_chart > cap_threshold]
        df_chart.fillna(0, inplace=True)
        if groupby_cols:
            df_chart = df_chart.loc[:, (df_chart != 0).any(axis=0)]

    if sorted is not None:
        if sorted == "index":
            df_chart = df_chart.sort_index()
        else:
            if groupby_cols:
                df_chart = df_chart.sort_values(
                    by=df_chart.index.values.tolist(), axis=1, ascending=False
                )
            else:
                df_chart = df_chart.sort_values(ascending=False)

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

    if filename:
        chart_filepath = CHART_FOLDER / filename
        if filename and not filename.endswith(".pdf"):
            filename += ".pdf"
        plt.savefig(
            chart_filepath, dpi=1200, format="pdf", pad_inches=0.5, bbox_inches="tight"
        )
    else:
        plt.show()
