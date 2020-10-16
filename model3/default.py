
# ------------------------------------------------------------------------------
# Copyright (c) Microsoft
# Licensed under the MIT License.
# Written by Ke Sun (sunk@mail.ustc.edu.cn)
# ------------------------------------------------------------------------------

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from yacs.config import CfgNode as CN


_C = CN()
#
# # common params for NETWORK
# _C.MODEL = CN()
# _C.MODEL.NAME = 'seg_hrnet'
# _C.MODEL.PRETRAINED = ''
# _C.MODEL.EXTRA = CN(new_allowed=True)
#
# # stage2
# _C.MODEL.EXTRA.STAGE2 = CN()
# _C.MODEL.EXTRA.STAGE2.NUM_MODULES = 1
# _C.MODEL.EXTRA.STAGE2.NUM_BRANCHES = 2
# _C.MODEL.EXTRA.STAGE2.BLOCK = 'BASIC'
# _C.MODEL.EXTRA.STAGE2.NUM_BLOCKS = [4, 4]
# _C.MODEL.EXTRA.STAGE2.NUM_CHANNELS = [48, 96]
# _C.MODEL.EXTRA.STAGE2.FUSE_METHOD = 'SUM'
#
# # stage3
# _C.MODEL.EXTRA.STAGE3 = CN()
# _C.MODEL.EXTRA.STAGE3.NUM_MODULES = 4
# _C.MODEL.EXTRA.STAGE3.NUM_BRANCHES = 3
# _C.MODEL.EXTRA.STAGE3.BLOCK = 'BASIC'
# _C.MODEL.EXTRA.STAGE3.NUM_BLOCKS = [4, 4, 4]
# _C.MODEL.EXTRA.STAGE3.NUM_CHANNELS = [48, 96, 192]
# _C.MODEL.EXTRA.STAGE3.FUSE_METHOD = 'SUM'
#
# # stage4
# _C.MODEL.EXTRA.STAGE4 = CN()
# _C.MODEL.EXTRA.STAGE4.NUM_MODULES = 3
# _C.MODEL.EXTRA.STAGE4.NUM_BRANCHES = 4
# _C.MODEL.EXTRA.STAGE4.BLOCK = 'BASIC'
# _C.MODEL.EXTRA.STAGE4.NUM_BLOCKS = [4, 4, 4, 4]
# _C.MODEL.EXTRA.STAGE4.NUM_CHANNELS = [48, 96, 192, 384]
# _C.MODEL.EXTRA.STAGE4.FUSE_METHOD = 'SUM'

_C.MODEL = CN()
_C.MODEL.EXTRA = CN(new_allowed=True)
_C.MODEL.PRETRAINED_LAYERS = ['*']
_C.MODEL.STEM_INPLANES = 64
_C.MODEL.FINAL_CONV_KERNEL = 1
_C.MODEL.WITH_HEAD = True

_C.MODEL.EXTRA.STAGE2 = CN()
_C.MODEL.EXTRA.STAGE2.NUM_MODULES = 1
_C.MODEL.EXTRA.STAGE2.NUM_BRANCHES = 2
_C.MODEL.EXTRA.STAGE2.NUM_BLOCKS = [4, 4]
_C.MODEL.EXTRA.STAGE2.NUM_CHANNELS = [48, 96]
_C.MODEL.EXTRA.STAGE2.BLOCK = 'BASIC'
_C.MODEL.EXTRA.STAGE2.FUSE_METHOD = 'SUM'

_C.MODEL.EXTRA.STAGE3 = CN()
_C.MODEL.EXTRA.STAGE3.NUM_MODULES = 4
_C.MODEL.EXTRA.STAGE3.NUM_BRANCHES = 3
_C.MODEL.EXTRA.STAGE3.NUM_BLOCKS = [4, 4, 4]
_C.MODEL.EXTRA.STAGE3.NUM_CHANNELS = [48, 96, 192]
_C.MODEL.EXTRA.STAGE3.BLOCK = 'BASIC'
_C.MODEL.EXTRA.STAGE3.FUSE_METHOD = 'SUM'

_C.MODEL.EXTRA.STAGE4 = CN()
_C.MODEL.EXTRA.STAGE4.NUM_MODULES = 3
_C.MODEL.EXTRA.STAGE4.NUM_BRANCHES = 4
_C.MODEL.EXTRA.STAGE4.NUM_BLOCKS = [4, 4, 4, 4]
_C.MODEL.EXTRA.STAGE4.NUM_CHANNELS = [48, 96, 192, 384]
_C.MODEL.EXTRA.STAGE4.BLOCK = 'BASIC'
_C.MODEL.EXTRA.STAGE4.FUSE_METHOD = 'SUM'



