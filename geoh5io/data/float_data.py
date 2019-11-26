from .data import Data, PrimitiveTypeEnum


class FloatData(Data):
    @classmethod
    def primitive_type(cls) -> PrimitiveTypeEnum:
        return PrimitiveTypeEnum.FLOAT

    @property
    def values(self):
        if (getattr(self, "_values", None) is None) and self.existing_h5_entity:
            self._values = self.entity_type.workspace.fetch_values(self.uid)

        return self._values

    @values.setter
    def values(self, values):

        if self.existing_h5_entity:
            self._update_h5 = True

        self._values = values

    def __call__(self):
        return self.values
