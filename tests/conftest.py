"""
Test for SQS to DC tool
"""
import json
from pathlib import Path

import pystac
import pystac.collection
import pystac.item
import pytest
from datacube.utils import documents

from odc.stac import stac2ds

TEST_DATA_FOLDER: Path = Path(__file__).parent.joinpath("data")
GA_LANDSAT_STAC: str = "ga_ls8c_ard_3-1-0_088080_2020-05-25_final.stac-item.json"
GA_LANDSAT_ODC: str = "ga_ls8c_ard_3-1-0_088080_2020-05-25_final.odc-metadata.yaml"
SENTINEL_STAC_COLLECTION: str = "sentinel-2-l2a.collection.json"
SENTINEL_STAC: str = "S2A_28QCH_20200714_0_L2A.json"
SENTINEL_STAC_MS: str = "S2B_MSIL2A_20190629T212529_R043_T06VVN_20201006T080531.json"
SENTINEL_STAC_MS_RASTER_EXT: str = (
    "S2B_MSIL2A_20190629T212529_R043_T06VVN_20201006T080531_raster_ext.json"
)
SENTINEL_ODC: str = "S2A_28QCH_20200714_0_L2A.odc-metadata.json"
USGS_LANDSAT_STAC_v1b: str = "LC08_L2SR_081119_20200101_20200823_02_T2.json"
USGS_LANDSAT_STAC_v1: str = "LC08_L2SP_028030_20200114_20200824_02_T1_SR.json"
LIDAR_STAC: str = "lidar_dem.json"

# pylint: disable=redefined-outer-name


@pytest.fixture(scope="session")
def test_data_dir():
    return TEST_DATA_FOLDER


@pytest.fixture
def usgs_landsat_stac_v1():
    return pystac.item.Item.from_file(
        str(TEST_DATA_FOLDER.joinpath(USGS_LANDSAT_STAC_v1))
    )


@pytest.fixture
def usgs_landsat_stac_v1b():
    return pystac.item.Item.from_file(
        str(TEST_DATA_FOLDER.joinpath(USGS_LANDSAT_STAC_v1b))
    )


@pytest.fixture
def ga_landsat_stac():
    return pystac.item.Item.from_file(str(TEST_DATA_FOLDER.joinpath(GA_LANDSAT_STAC)))


@pytest.fixture
def lidar_stac():
    return pystac.item.Item.from_file(str(TEST_DATA_FOLDER.joinpath(LIDAR_STAC)))


@pytest.fixture
def ga_landsat_odc():
    metadata = yield from documents.load_documents(
        TEST_DATA_FOLDER.joinpath(GA_LANDSAT_ODC)
    )
    return metadata


@pytest.fixture
def sentinel_stac():
    return pystac.item.Item.from_file(str(TEST_DATA_FOLDER.joinpath(SENTINEL_STAC)))


@pytest.fixture
def sentinel_stac_ms_json():
    with TEST_DATA_FOLDER.joinpath(SENTINEL_STAC_MS).open("r") as f:
        return json.load(f)


@pytest.fixture
def sentinel_stac_ms(sentinel_stac_ms_json):
    metadata = dict(sentinel_stac_ms_json)
    return pystac.item.Item.from_dict(metadata)


@pytest.fixture
def sentinel_stac_ms_no_ext(sentinel_stac_ms_json):
    metadata = dict(sentinel_stac_ms_json)
    metadata["stac_extensions"] = []
    return pystac.item.Item.from_dict(metadata)


@pytest.fixture
def sentinel_stac_ms_with_raster_ext():
    return pystac.item.Item.from_file(
        str(TEST_DATA_FOLDER.joinpath(SENTINEL_STAC_MS_RASTER_EXT))
    )


@pytest.fixture
def sentinel_stac_collection():
    return pystac.collection.Collection.from_file(
        str(TEST_DATA_FOLDER.joinpath(SENTINEL_STAC_COLLECTION))
    )


@pytest.fixture
def sentinel_odc():
    return pystac.item.Item.from_file(str(TEST_DATA_FOLDER.joinpath(SENTINEL_ODC)))


@pytest.fixture
def s2_dataset(sentinel_stac_ms_with_raster_ext):
    (ds,) = stac2ds(
        [sentinel_stac_ms_with_raster_ext], cfg={"*": {"warnings": "ignore"}}
    )
    yield ds
