# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: pymammotion/proto/common.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CommDataCouple(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
