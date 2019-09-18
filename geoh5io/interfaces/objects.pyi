from dataclasses import dataclass
from enum import IntEnum
from typing import *


from . import shared




class InvalidObjectOperation(Exception):
    message: Optional[str] = ""




class ObjectClass(IntEnum):
    UNKNOWN = 0
    POINTS = 1
    CURVE = 2
    SURFACE = 3
    GRID2D = 4
    DRILLHOLE = 5
    BLOCKMODEL = 6
    OCTREE = 7
    GEOIMAGE = 8
    LABEL = 9




@dataclass
class Object:
    base_: Optional[shared.Entity] = None
    allow_move: Optional[bool] = True

@dataclass
class Points:
    base_: Optional[Object] = None

@dataclass
class Curve:
    base_: Optional[Object] = None

@dataclass
class Surface:
    base_: Optional[Object] = None

@dataclass
class Grid2D:
    base_: Optional[Object] = None

@dataclass
class Drillhole:
    base_: Optional[Object] = None

@dataclass
class BlockModel:
    base_: Optional[Object] = None

@dataclass
class Octree:
    base_: Optional[Object] = None

@dataclass
class GeoImage:
    base_: Optional[Object] = None

@dataclass
class Label:
    base_: Optional[Object] = None

@dataclass
class ObjectQuery:
    name: Optional[str] = ""
    type: Optional[shared.Uuid] = None
    in_group: Optional[shared.Uuid] = None
    recursive: Optional[bool] = False

@dataclass
class GeometryTransformation:
    translation: Optional[shared.Coord3D] = None
    rotation_deg: Optional[float] = 0.0




class ObjectService:
    def get_type(
        self,
        object_class: int,
    ) -> shared.Uuid:
        ...
    def get_class(
        self,
        type: shared.Uuid,
    ) -> int:
        ...
    def get_all(
        self,
    ) -> List[Object]:
        ...
    def find(
        self,
        query: ObjectQuery,
    ) -> List[Object]:
        ...
    def set_allow_move(
        self,
        objects: List[shared.Uuid],
        allow: bool,
    ) -> None:
        ...
    def move_to_group(
        self,
        objects: List[shared.Uuid],
        destination_group: shared.Uuid,
    ) -> None:
        ...
    def get(
        self,
        uid: shared.Uuid,
    ) -> Object:
        ...
    def narrowPoints(
        self,
        uid: shared.Uuid,
    ) -> Points:
        ...
    def narrowCurve(
        self,
        uid: shared.Uuid,
    ) -> Curve:
        ...
    def narrowSurface(
        self,
        uid: shared.Uuid,
    ) -> Surface:
        ...
    def narrowGrid2D(
        self,
        uid: shared.Uuid,
    ) -> Grid2D:
        ...
    def narrowDrillhole(
        self,
        uid: shared.Uuid,
    ) -> Drillhole:
        ...
    def narrowBlockModel(
        self,
        uid: shared.Uuid,
    ) -> BlockModel:
        ...
    def narrowOctree(
        self,
        uid: shared.Uuid,
    ) -> Octree:
        ...
    def narrowGeoImage(
        self,
        uid: shared.Uuid,
    ) -> GeoImage:
        ...
    def narrowLabel(
        self,
        uid: shared.Uuid,
    ) -> Label:
        ...
    def createAnyObject(
        self,
        type: shared.Uuid,
        name: str,
        parent_group: shared.Uuid,
        attributes: Dict[str, str],
    ) -> Object:
        ...
    def transform(
        self,
        objects: List[shared.Uuid],
        transformation: GeometryTransformation,
    ) -> None:
        ...
    def set_public(
        self,
        entities: List[shared.Uuid],
        is_public: bool,
    ) -> None:
        ...
    def set_visible(
        self,
        entities: List[shared.Uuid],
        visible: bool,
    ) -> None:
        ...
    def set_allow_delete(
        self,
        entities: List[shared.Uuid],
        allow: bool,
    ) -> None:
        ...
    def set_allow_rename(
        self,
        entities: List[shared.Uuid],
        allow: bool,
    ) -> None:
        ...
    def rename(
        self,
        entities: shared.Uuid,
        new_name: str,
    ) -> None:
        ...
