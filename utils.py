from multiprocessing.dummy import Array
import numpy as np
import pandas as pd
from numpy.typing import ArrayLike

from functools import partial


def map_multiple_choices(entries: str, entries_map: dict[str, int]) -> ArrayLike:
    """Map each sample to their list of motivations - spiking a one whenever that motivation was specified"""
    values = np.zeros(shape=len(entries_map), dtype=int)
    for choice in entries_map.keys():
        if choice in entries:
            values[entries_map[choice]] = 1
    return values


def quick_purge_presets(mm, preset_choices):
    for m in preset_choices:
        mm = mm.replace(m, "")
    mm = mm.replace(",", "").strip()
    return mm


def process_multiple_choices(
    data: pd.Series, choices: list[str]
) -> tuple[tuple[str], ArrayLike]:
    """"""
    quick_purge = partial(quick_purge_presets, preset_choices=choices)
    extra_choices = set(
        filter(lambda m: len(m), map(quick_purge, data.values.tolist()))
    )
    all_choices = choices + tuple(extra_choices)
    values_map = {k.strip(): i for i, k in enumerate(all_choices)}
    map_func = partial(map_multiple_choices, entries_map=values_map)
    return tuple(values_map.keys()), np.vstack(data.map(map_func)).T
