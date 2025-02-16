#!/usr/bin/env python3


import time
import os
import random

# random.seed(13)

# Define colors
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
NC = '\033[0m' # No Color

X = ["Left", "Right"]
Y = ["Superior", "Inferior"]
Z = ["Anterior", "Posterior"]

def ct_iso():
    # Generate random CT ISO positions within specified ranges
    x = round(random.uniform(-2, 2), 1)
    y = round(random.uniform(50, 100), 1)
    z = round(random.uniform(-30, 0), 1)
    return x, y, z

def dep():
    # Generate random displacements and directions
    dx = round(random.uniform(0.1, 10.0), 1)
    dy = round(random.uniform(0.1, 10.0), 1)
    dz = round(random.uniform(0.1, 10.0), 1)
    vx = random.randint(0, 1)
    vy = random.randint(0, 1)
    vz = random.randint(0, 1)
    return dx, dy, dz, vx, vy, vz

def trt_iso(x, y, z):
    # x, y, z = ct_iso()
    dx, dy, dz, vx, vy, vz = dep()

    # Calculate new ISO positions based on directions
    new_x = x + dx if vx == 1 else x - dx
    new_y = y + dy if vy == 0 else y - dy
    new_z = z + dz if vz == 0 else z - dz


    # Display the resulting treatment ISO positions
    print("  Displacements to Apply:")
    if random.randint(1, 3) == 1:
        print(f"\t{YELLOW}{dx:.1f} {X[vx]}{NC}")
        print("\n  Treatment ISO Position: ", end='')
        input()
        print(f"\t{RED}x: {new_x:.1f}{NC} ", end='')
    elif random.randint(1, 3) == 2:
        print(f"\t{YELLOW}{dy:.1f} {Y[vy]}{NC}")
        print("\n  Treatment ISO Position: ", end='')
        input()
        print(f"\t{RED}y: {new_y:.1f}{NC} ", end='')
    else:
        print(f"\t{YELLOW}{dz:.1f} {Z[vz]}{NC}")
        print("\n  Treatment ISO Position: ", end='')
        input()
        print(f"\t{RED}z: {new_z:.1f}{NC} ", end='')



def main():
    i = -1
    x, y, z = ct_iso()
    t0, t1 = 0, 0

    while(True):
        os.system("clear")
        time.sleep(0.2)
        i+=1
        if i % 10 == 0:
            # regenerate new ct iso after 10 essaie
            x, y, z = ct_iso()
        else:
            print(f"  last exercise: {RED}{t1-t0:.1f}{NC}s")
        # print(f"\ttime: {tm-i}s\n")

        # Display initial positions and displacements
        t0=time.time()
        print("\n\tExercise: %i\n" % (i+1))
        print("  Initial CT ISO Position:")
        print(f"{GREEN}\tx: {x:.1f}\n\ty: {y:.1f}\n\tz: {z:.1f}\n{NC}")

        trt_iso(x, y, z)
        t1=time.time()
        # input("\n  Press Enter to continue...")
        input()

if __name__ == '__main__':
    main()
