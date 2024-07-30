from pypower.api import runpf,ppoption
import numpy as np

# Define your custom power network data without generators


# Run power flow
def lf(network):
    options = ppoption(VERBOSE=0, OUT_ALL=0) #pour ne pas avoir le résultat affiché sur la console
    results, success = runpf(network,options)

    if success:
        # Extract bus voltages and angles
        S_base=network["baseMVA"]
        V_base=network["bus"][0][9]
        bus = results['bus']
        V_mag = bus[:, 7]  # Column 8 is voltage magnitude
        V_ang = bus[:, 8]  # Column 9 is voltage angle in degrees

        # Convert angles to radians for current calculation
        V_ang_rad = np.deg2rad(V_ang)

        # Calculate complex voltages
        V = V_mag * (np.cos(V_ang_rad) + 1j * np.sin(V_ang_rad))
        # Extract branch data
        branch = results['branch']
        from_bus = branch[:, 0].astype(int) - 1  # Branch starting buses (convert to zero-based indexing)
        to_bus = branch[:, 1].astype(int) - 1    # Branch ending buses (convert to zero-based indexing)
        r = branch[:, 2]                         # Branch resistance
        x = branch[:, 3]                         # Branch reactance

        # Calculate branch admittance
        Z = r + 1j * x
        Y = 1 / Z

        # Calculate currents in each branch
        I = np.zeros(len(branch), dtype=complex)
        for i in range(len(branch)):
            I[i] = (V[from_bus[i]] - V[to_bus[i]]) * Y[i]*(S_base/V_base*1000)

        # # Print results (pour regarder les valuers de sortie)
        # print("Bus Voltages (p.u.):")
        # for i, (mag, ang) in enumerate(zip(V_mag, V_ang)):
        #     print(f"Bus {i+1}: {mag:.4f} ∠ {ang:.2f}°")

        # print("\nBranch Currents (p.u.):")
        # for i, current in enumerate(I):
        #     print(f"Branch {from_bus[i]+1}-{to_bus[i]+1}: {abs(current):.4f} ∠ {np.angle(current, deg=True):.2f}°")
        return I,V
    else:
        print("Power flow did not converge.")
        return [],[]
    