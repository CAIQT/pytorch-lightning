# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Test deprecated functionality which will be removed in v1.8.0."""
import pytest

from pytorch_lightning import LightningModule
from pytorch_lightning.utilities.enums import DistributedType


def test_v1_8_0_deprecated_distributed_type_enum():

    with pytest.deprecated_call(match="has been deprecated in v1.6 and will be removed in v1.8."):
        _ = DistributedType.DDP


@pytest.mark.parametrize("container", [{}, {"batch_size": 4}])
def test_deprecated_save_hyperparameters_container(container):
    class HyperparameterModule(LightningModule):
        def __init__(self, c):
            super().__init__()
            self.save_hyperparameters(c)

    with pytest.deprecated_call(match="Passing a container to `save_hyperparameters` has been deprecated in v1.6"):
        HyperparameterModule(container)