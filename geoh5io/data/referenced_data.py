from geoh5io.data import Data
from geoh5io.data import PrimitiveTypeEnum


class ReferencedData(Data):
    @classmethod
    def primitive_type(cls) -> PrimitiveTypeEnum:
        return PrimitiveTypeEnum.REFERENCED

    # TODO: implement specialization to access values.
    # Stored as a 1D array of UTF-8 encoded, variable-length string type designating a file name.
    # For each file name within "Data", an opaque data set named after the filename must
    # be added under the Data instance, containing a complete binary dump of the file.
    # Different files (under the same object/group) must be saved under different names.
    # No data value : empty string
