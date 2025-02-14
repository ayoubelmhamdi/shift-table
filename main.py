#!/usr/bin/env python3

import time

X = ["Left","Right"]
Y = ["Superior", "Inferior"]
Z = ["Anterior", "Posterior"]

def ct_iso():
    # use random values.
    x = 10.7 # [-10, 10]
    y = 10.7 # [0, 100]
    z = 10.7 # [-30, 0]

    return x, y, z


def dep():
    # use random values.
    dx = 3
    dy = 3
    dz = 3

    # use random values 0 or 1.
    vx = 0
    vy = 1
    vz = 1
    return dx, dy, dz, vx, vy, vz


def trt_iso():
    x, y, z = ct_iso()
    dx, dy, dz, vx, vy, vz = dep()

    print(f"x: {x}\ny: {y}\nz: {z}")

    print(f"{dx} {X[vx]}")
    print(f"{dy} {Y[vy]}")
    print(f"{dz} {Z[vz]}")

    time.sleep(3)
    print("\n\n")
    print(f"x: {x}\ny: {y}\nz: {z}")



def main():
    trt_iso()

if __name__ == '__main__':
    main()
