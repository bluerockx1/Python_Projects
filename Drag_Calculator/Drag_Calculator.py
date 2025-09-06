def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    while True:  # Loop to allow repeated calculations
        print("\nDrag Calculator")
        print("\nChoose an option:")
        print("1. Calculate Air Density")
        print("2. Enter Air Density")
        choice = input("Enter 1 or 2: ")

        if choice == '1':
            print("\nSelect units:")
            print("1. SI units (kg/m^3, m/s)")
            print("2. Imperial units (mph, ft^2)")
            unit_choice = input("Enter 1 or 2: ")

            if unit_choice == '1':
                P_Pa = get_float("Enter Pressure in Pascals (Pa): ")
                T_K = get_float("Enter Temperature in Kelvin (K): ")
                v_mps = get_float("Enter Velocity in meters per second (m/s): ")
                Cd = get_float("Enter Drag Coefficient (dimensionless): ")
                A_m2 = get_float("Enter Area in square meters (m^2): ")
                rho = P_Pa / (287.05 * T_K)

            elif unit_choice == '2':
                P_psi = get_float("Enter Pressure in pounds per square inch (psi): ")
                T_F = get_float("Enter Temperature in Fahrenheit (°F): ")
                v_mph = get_float("Enter Velocity in miles per hour (mph): ")
                Cd = get_float("Enter Drag Coefficient (dimensionless): ")
                A_ft2 = get_float("Enter Area in square feet (ft^2): ")
                P_Pa = P_psi * 6894.76
                T_K = (T_F - 32) * 5 / 9 + 273.15
                v_mps = v_mph * 0.44704
                A_m2 = A_ft2 * 0.092903
                rho = P_Pa / (287.05 * T_K)

            else:
                print("Invalid unit choice.")
                continue

        elif choice == '2':
            print("\nSelect units:")
            print("1. SI units (kg/m^3, m/s)")
            print("2. Imperial units (slugs/ft^3, mph, ft^2)")
            unit_choice = input("Enter 1 or 2: ")

            if unit_choice == '1':
                rho = get_float("Enter Air Density in kg/m^3: ")
                v_mps = get_float("Enter Velocity in meters per second (m/s): ")
                Cd = get_float("Enter Drag Coefficient (dimensionless): ")
                A_m2 = get_float("Enter Area in square meters (m^2): ")

            elif unit_choice == '2':
                rho_slug_ft3 = get_float("Enter Air Density in slugs/ft^3: ")
                v_mph = get_float("Enter Velocity in miles per hour (mph): ")
                Cd = get_float("Enter Drag Coefficient (dimensionless): ")
                A_ft2 = get_float("Enter Area in square feet (ft^2): ")
                rho = rho_slug_ft3 * 515.3788
                v_mps = v_mph * 0.44704
                A_m2 = A_ft2 * 0.092903

            else:
                print("Invalid unit choice.")
                continue

        else:
            print("Invalid choice.")
            continue

        # Drag Force Calculation
        Fd = 0.5 * rho * v_mps ** 2 * Cd * A_m2
        print(f"\nCalculated Drag Force: {Fd:.2f} N")

        # Ask to repeat
        repeat_calc = input("\nDo you want to calculate again? (y/n) [default: y]: ").lower()
        if repeat_calc == '' or repeat_calc == 'y':
            continue  # repeat the loop
        else:
            print("Thank you for using the Drag Calculator!")
            break  # exit loop


if __name__ == "__main__":
    main()
