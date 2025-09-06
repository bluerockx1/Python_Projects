def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    while True:
        print("\nLift Calculator")
        print("\nChoose an option:")
        print("1. SI units (kg/m^3, m/s)")
        print("2. Imperial units (mph, ft^2)")
        unit_choice = input("Enter 1 or 2: ")

        if unit_choice == '1':
            rho = get_float("Enter Air Density (kg/m^3): ")
            v_mps = get_float("Enter Velocity in meters per second (m/s): ")
            Cl = get_float("Enter Lift Coefficient (dimensionless): ")
            A_m2 = get_float("Enter Wing Area in square meters (m^2): ")
        elif unit_choice == '2':
            rho_slug_ft3 = get_float("Enter Air Density in slugs/ft^3: ")
            v_mph = get_float("Enter Velocity in miles per hour (mph): ")
            Cl = get_float("Enter Lift Coefficient (dimensionless): ")
            A_ft2 = get_float("Enter Wing Area in square feet (ft^2): ")
            # Imperial to SI conversions
            rho = rho_slug_ft3 * 515.378818
            v_mps = v_mph * 0.44704
            A_m2 = A_ft2 * 0.092903
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        # Lift calculation
        L = 0.5 * rho * v_mps ** 2 * Cl * A_m2
        L_lbf = L * 0.224809  # Newtons to pounds-force
        print(f"\nCalculated Lift: {L:.2f} N ({L_lbf:.2f} lbf)")

        # Ask to repeat
        repeat_calc = input("\nDo you want to calculate again? (y/n) [default: y]: ").lower()
        if repeat_calc == '' or repeat_calc == 'y':
            continue
        else:
            print("Thank you for using the Lift Calculator!")
            break


if __name__ == "__main__":
    main()