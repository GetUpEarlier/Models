# -*- coding: utf-8 -*-
# MegEngine is Licensed under the Apache License, Version 2.0 (the "License")
#
# Copyright (c) 2014-2020 Megvii Inc. All rights reserved.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT ARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

from megengine import hub

from official.vision.detection import models


class CustomFreeAnchorConfig(models.FreeAnchorConfig):
    def __init__(self):
        super().__init__()

        self.backbone = "resnet101"

        # ------------------------ training cfg ---------------------- #
        self.max_epoch = 36
        self.lr_decay_stages = [24, 32]


@hub.pretrained(
    "https://data.megengine.org.cn/models/weights/"
    "freeanchor_coco_res101_2x_800size_43dot3_61b20bfa.pkl"
)
def freeanchor_res101_coco_2x_800size(**kwargs):
    r"""
    RetinaNet trained from COCO dataset.
    `"RetinaNet" <https://arxiv.org/abs/1708.02002>`_
    `"FPN" <https://arxiv.org/abs/1612.03144>`_
    `"COCO" <https://arxiv.org/abs/1405.0312>`_
    """
    cfg = models.FreeAnchorConfig()
    return models.FreeAnchor(cfg, **kwargs)


Net = models.FreeAnchor
Cfg = CustomFreeAnchorConfig
