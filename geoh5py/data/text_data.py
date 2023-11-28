#  Copyright (c) 2023 Mira Geoscience Ltd.
#
#  This file is part of geoh5py.
#
#  geoh5py is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  geoh5py is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with geoh5py.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

import json

import numpy as np

from .data import Data
from .primitive_type_enum import PrimitiveTypeEnum


class TextData(Data):
    _values: np.ndarray | str | None

    @classmethod
    def primitive_type(cls) -> PrimitiveTypeEnum:
        return PrimitiveTypeEnum.TEXT

    @property
    def values(self) -> np.ndarray | str | None:
        """
        :obj:`str` Text value.
        """
        if (getattr(self, "_values", None) is None) and self.on_file:
            values = self.workspace.fetch_values(self)

            if isinstance(values, np.ndarray) and values.dtype == object:
                values = values.astype(str)

            if isinstance(values, (np.ndarray, str, type(None))):
                self._values = values

        return self._values

    @values.setter
    def values(self, values: np.ndarray | str | None):
        if isinstance(values, bytes):
            values = values.decode()

        if isinstance(values, np.ndarray) and values.dtype == object:
            values = values.astype(str)

        if (not isinstance(values, (str, type(None), np.ndarray))) or (
            isinstance(values, np.ndarray) and values.dtype.kind not in ["U", "S"]
        ):
            raise ValueError(
                f"Input 'values' for {self} must be of type {np.ndarray}  str or None."
            )

        self._values = values

        self.workspace.update_attribute(self, "values")


class CommentsData(Data):
    """
    Comments added to an Object or Group.
    Stored as a list of dictionaries with the following keys:

        .. code-block:: python

            comments = [
                {
                    "Author": "username",
                    "Date": "2020-05-21T10:12:15",
                    "Text": "A text comment."
                },
            ]
    """

    @classmethod
    def primitive_type(cls) -> PrimitiveTypeEnum:
        return PrimitiveTypeEnum.TEXT

    @property
    def values(self) -> list[dict] | None:
        """
        :obj:`list` List of comments
        """
        if (getattr(self, "_values", None) is None) and self.on_file:
            comment_str = self.workspace.fetch_values(self)

            if isinstance(comment_str, str):
                self._values = json.loads(comment_str)["Comments"]

        return self._values

    @values.setter
    def values(self, values):
        self.workspace.update_attribute(self, "values")

        if values is not None:
            for value in values:
                assert isinstance(value, dict), (
                    f"Error setting CommentsData with expected input of type list[dict].\n"
                    f"Input {type(values)} provided."
                )
                assert list(value.keys()) == ["Author", "Date", "Text"], (
                    f"Comment dictionaries must include keys 'Author', 'Date' and 'Text'.\n"
                    f"Keys {list(value.keys())} provided."
                )

        self._values = values
        self.workspace.update_attribute(self, "values")


class MultiTextData(Data):
    _values: np.ndarray | str | None

    @classmethod
    def primitive_type(cls) -> PrimitiveTypeEnum:
        return PrimitiveTypeEnum.MULTI_TEXT

    @property
    def values(self) -> np.ndarray | str | None:
        """
        :obj:`str` Text value.
        """
        if (getattr(self, "_values", None) is None) and self.on_file:
            values = self.workspace.fetch_values(self)
            if isinstance(values, (np.ndarray, str, type(None))):
                self._values = values

        return self._values

    @values.setter
    def values(self, values: np.ndarray | str | None):
        self._values = values

        if not isinstance(values, (np.ndarray, str, type(None))):
            raise ValueError(
                f"Input 'values' for {self} must be of type {np.ndarray}  str or None."
            )

        self.workspace.update_attribute(self, "values")
