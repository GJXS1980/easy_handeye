#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tf

# (r, p, y) = tf.transformations.euler_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w])
(r, p, y) = tf.transformations.euler_from_quaternion([x, y, z, w])
print((r, p, y))
