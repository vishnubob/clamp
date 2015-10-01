#!/usr/bin/env python

from scad import *
import os

class Clamp(SCAD_Object):
    head_corner_dia = 3
    height = 9.5
    head_width = 23 - head_corner_dia
    head_depth = 40 - head_corner_dia
    head_hole_dia = 5.5
    body_width = 113 - head_width
    body_depth = 30
    channel_width = 60
    channel_dia = 5.5

    def scad(self):
        head = Cube(x=self.head_width, y=self.head_depth, z=self.height, center=True)
        head_hole = Cylinder(dia=self.head_hole_dia, h=self.height + 1, center=True)
        head_corner = Cylinder(dia=self.head_corner_dia, h=self.height, center=True, fn=20)
        head_corner1 = Translate(x=self.head_width / -2.0 + self.head_corner_dia / 4.0, y=self.head_depth / 2.0 - self.head_corner_dia / 4.0)(head_corner)
        head_corner2 = Translate(x=self.head_width / -2.0 + self.head_corner_dia / 4.0, y=self.head_depth / -2.0 + self.head_corner_dia / 4.0)(head_corner)
        head_corner3 = Translate(x=self.head_width / 2.0 - self.head_corner_dia / 4.0, y=self.head_depth / 2.0 - self.head_corner_dia / 4.0)(head_corner)
        head_corner4 = Translate(x=self.head_width / 2.0 - self.head_corner_dia / 4.0, y=self.head_depth / -2.0 + self.head_corner_dia / 4.0)(head_corner)
        head = Hull()(head, head_corner1, head_corner2, head_corner3, head_corner4)
        head = Difference()(head, head_hole)
        body = Cube(x=self.body_width, y=self.body_depth, z=self.height, center=True)
        # bevel
        bevel = Cube(x=self.body_width, y=self.body_depth + 2, z=self.height, center=True)
        x_offset = self.body_width / -2.0
        bevel = Translate(x=x_offset, z=2)(bevel)
        bevel = Rotate(y=30)(bevel)
        x_offset = (self.body_width + self.head_width / 2.0) + 4
        bevel = Translate(x=x_offset)(bevel)
        # channel
        channel = Cube(x=self.channel_width, y=self.channel_dia, z=self.height + 1, center=True)
        channel_end = Cylinder(dia=self.channel_dia, h=self.height + 1, center=True)
        x_offset = (self.channel_width + self.channel_dia) / 2.0 - self.channel_dia / 2.0
        channel_end1 = Translate(x=x_offset)(channel_end)
        x_offset = (self.channel_width + self.channel_dia) / -2.0 + self.channel_dia / 2.0
        channel_end2 = Translate(x=x_offset)(channel_end)
        channel = Union()(channel, channel_end1, channel_end2)
        width = self.channel_width + self.channel_dia
        body = Difference()(body, channel)
        x_offset = (self.body_width + self.head_width) / 2.0
        body = Translate(x=x_offset)(body)
        clamp = Union()(head, body)
        clamp = Difference()(clamp, bevel)
        return clamp

clamp = Clamp()
clamp = SCAD_Globals(fn=40)(clamp)
clamp.render("clamp.scad")
if not os.path.exists("clamp.stl"):
    clamp.render("clamp.stl")

