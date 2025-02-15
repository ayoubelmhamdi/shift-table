#!/usr/bin/env python3


import time
import os
import random

random.seed(13+1)

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
        print(f"\t{dx:.1f} {X[vx]}")
        print("\n  Treatment ISO Position: ", end='')
        # time.sleep(n)
        input()
        print(f"\n\tx: {new_x:.1f}")
    elif random.randint(1, 3) == 2:
        print(f"\t{dy:.1f} {Y[vy]}")
        print("\n  Treatment ISO Position: ", end='')
        # time.sleep(n)
        input()
        print(f"\n\ty: {new_y:.1f}")
    else:
        print(f"\t{dz:.1f} {Z[vz]}")
        print("\n  Treatment ISO Position: ", end='')
        # time.sleep(n)
        input()
        print(f"\n\tz: {new_z:.1f}")



def main():
    i = -1
    x, y, z = ct_iso()
    while(True):
        i+=1
        if i % 10 == 0:
            # regenerate new ct iso after 10 essaie
            x, y, z = ct_iso()
        os.system("clear")
        # print(f"\ttime: {tm-i}s\n")

        # Display initial positions and displacements
        t0=time.time()
        print("\n\tExercise: %i\n" % (i+1))
        print("  Initial CT ISO Position:")
        print(f"\tx: {x:.1f}\n\ty: {y:.1f}\n\tz: {z:.1f}\n")

        trt_iso(x, y, z)
        print(f"\n  finished in {time.time()-t0:.1f} seconds")
        # input("\n  Press Enter to continue...")
        input()

if __name__ == '__main__':
    main()
