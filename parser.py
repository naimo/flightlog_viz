#!/usr/bin/env python3

import numpy as np
import matplotlib
matplotlib.use('Qt4Agg')
import matplotlib.pyplot as plt


regex = r"temp = (\d+)\r\n" + \
          "pressure = (\d+)\r\n" \
          "gyro x=\s*(\-?\d+) y=\s*(\-?\d+) z=\s*(\-?\d+) acc x=\s*(\-?\d+) y=\s*(\-?\d+) z=\s*(\-?\d+)\r\n" \
          "mag x=\s*(\-?\d+) y=\s*(\-?\d+) z=\s*(\-?\d+)"

result = np.fromregex("data/data", regex,
            dtype=[ ('val',int),
                    ('temp',int),
                    ('gyro_x',int),
                    ('gyro_y',int),
                    ('gyro_z',int),
                    ('acc_x',int),
                    ('acc_y',int),
                    ('acc_z',int),
                    ('mag_x',int),
                    ('mag_y',int),
                    ('mag_z',int),])

plt.plot(result['acc_x'])
plt.plot(result['acc_y'])
plt.plot(result['acc_z'])

plt.plot(result['gyro_x'])
plt.plot(result['gyro_y'])
plt.plot(result['gyro_z'])
plt.show()