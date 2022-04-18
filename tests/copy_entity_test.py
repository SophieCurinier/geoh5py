#  Copyright (c) 2022 Mira Geoscience Ltd.
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

import os

import numpy as np
import pytest

from geoh5py.objects import Curve, Octree, Points, Surface
from geoh5py.shared.utils import compare_entities
from geoh5py.workspace import Workspace


def test_copy_entity(tmp_path):

    # Generate a random cloud of points
    n_data = 12
    xyz = np.random.randn(n_data, 3)
    objects = {
        Points: {"name": "Something", "vertices": np.random.randn(n_data, 3)},
        Surface: {
            "name": "Surface",
            "vertices": np.random.randn(n_data, 3),
            "cells": np.unique(
                np.random.randint(0, xyz.shape[0] - 1, (xyz.shape[0], 3)), axis=1
            ),
        },
        Curve: {
            "name": "Curve",
            "vertices": np.random.randn(n_data, 3),
        },
        Octree: {
            "origin": [0, 0, 0],
            "u_count": 32,
            "v_count": 16,
            "w_count": 8,
            "u_cell_size": 1.0,
            "v_cell_size": 1.0,
            "w_cell_size": 2.0,
            "rotation": 45,
        },
    }

    h5file_path = os.path.join(tmp_path, "testProject.geoh5")

    # Create a workspace
    workspace = Workspace(h5file_path)
    for obj, kwargs in objects.items():
        entity = obj.create(workspace, **kwargs)

        if getattr(entity, "vertices", None) is not None:
            values = np.random.randn(entity.n_vertices)
        else:
            values = np.random.randn(entity.n_cells)

        data = entity.add_data({"DataValues": {"values": values}})

    with pytest.raises(ValueError) as excinfo:
        workspace.copy_to_parent(entity, data)
    assert "Input 'parent' should be of type (ObjectBase, Group, Workspace)" in str(
        excinfo.value
    )

    workspace = Workspace(h5file_path)
    new_workspace = Workspace(os.path.join(tmp_path, "testProject_2.geoh5"))
    for entity in workspace.objects:
        entity.copy(parent=new_workspace)

    for entity in workspace.objects:

        # Read the data back in from a fresh workspace
        rec_entity = new_workspace.get_entity(entity.uid)[0]
        rec_data = new_workspace.get_entity(entity.children[0].uid)[0]

        compare_entities(entity, rec_entity, ignore=["_parent"])
        compare_entities(entity.children[0], rec_data, ignore=["_parent"])
