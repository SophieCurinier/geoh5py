from __future__ import annotations

import uuid
from typing import TYPE_CHECKING, Optional, Type, cast

from geoh5io.shared import EntityType

from .color_map import ColorMap
from .primitive_type_enum import PrimitiveTypeEnum

if TYPE_CHECKING:
    from geoh5io import workspace
    from . import data


class DataType(EntityType):
    def __init__(self, workspace: 'workspace.Workspace', uid: uuid.UUID, primitive_type:
    PrimitiveTypeEnum):
        super().__init__(workspace, uid)
        self._primitive_type = primitive_type
        # TODO: define properties and setters
        self._color_map: Optional[ColorMap] = None
        self._units = None

    @property
    def units(self) -> Optional[str]:
        return self._units

    @property
    def primitive_type(self) -> PrimitiveTypeEnum:
        return self._primitive_type

    @classmethod
    def find(cls, workspace: 'workspace.Workspace', type_uid: uuid.UUID) -> Optional[DataType]:
        return cast(DataType, workspace.find_type(type_uid, cls))

    @classmethod
    def create(cls, data_class: Type["data.Data"]) -> DataType:
        """ Creates a new instance of GroupType with the primitive type from the given Data
        implementation class.

        :param data_class: A Data implementation class.
        :return: A new instance of DataType.
        """
        uid = uuid.uuid4()
        primitive_type = data_class.primitive_type()
        return DataType(uid, primitive_type)
