from pypower.api import runpf 
import numpy as np

# Define your custom power network data without generators


# Run power flow
def lf(network):
    results, success = runpf(network)

    if success:
        # Extract bus voltages and angles
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
        b = branch[:, 4]                         # Line charging susceptance
        tap = branch[:, 8]                       # Transformer tap ratio
        tap[tap == 0] = 1.0                      # Set tap to 1 where not specified

        # Calculate branch admittance
        Z = r + 1j * x
        Y = 1 / Z
        Y = Y / tap

        # Calculate currents in each branch
        I = np.zeros(len(branch), dtype=complex)
        for i in range(len(branch)):
            I[i] = (V[from_bus[i]] - V[to_bus[i]]) * Y[i]

        # Print results
        print("Bus Voltages (p.u.):")
        for i, (mag, ang) in enumerate(zip(V_mag, V_ang)):
            print(f"Bus {i+1}: {mag:.4f} ∠ {ang:.2f}°")

        print("\nBranch Currents (p.u.):")
        for i, current in enumerate(I):
            print(f"Branch {from_bus[i]+1}-{to_bus[i]+1}: {abs(current):.4f} ∠ {np.angle(current, deg=True):.2f}°")
    else:
        print("Power flow did not converge.")
    return 0