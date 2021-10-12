""" Indexing related helper methods.
"""
from ._grouper import group_by_nothing, solar_offset
from ._index import (
    all_datasets,
    bin_dataset_stream,
    bin_dataset_stream2,
    chop_query_by_time,
    chopped_dss,
    count_by_month,
    count_by_year,
    dataset_count,
    from_metadata_stream,
    from_yaml_doc_stream,
    month_range,
    ordered_dss,
    parse_doc_stream,
    patch_urls,
    product_from_yaml,
    season_range,
    time_range,
)
from ._utm import mk_utm_gs, utm_region_code, utm_tile_dss, utm_zone_to_epsg
from ._uuid import odc_uuid

__all__ = (
    "from_yaml_doc_stream",
    "from_metadata_stream",
    "parse_doc_stream",
    "bin_dataset_stream",
    "bin_dataset_stream2",
    "dataset_count",
    "count_by_year",
    "count_by_month",
    "chop_query_by_time",
    "time_range",
    "month_range",
    "season_range",
    "ordered_dss",
    "chopped_dss",
    "all_datasets",
    "product_from_yaml",
    "patch_urls",
    "odc_uuid",
    "utm_region_code",
    "utm_zone_to_epsg",
    "utm_tile_dss",
    "mk_utm_gs",
    "group_by_nothing",
    "solar_offset",
)
