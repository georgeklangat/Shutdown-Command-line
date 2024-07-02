import os
import platform


def shutdown_system():
    """Shutdown the computer."""
    if platform.system() == 'Windows':
        os.system("shutdown /s /t 3")
    else:
        os.system("shutdown -h +3")


def restart_system():
    """Restart the computer."""
    if platform.system() == 'Windows':
        os.system("shutdown /r /t 3")
    else:
        os.system("shutdown -r +3")


def main():
    """Main function to prompt user and perform action based on input."""
    while True:
        choice = input("What would you like to do? (shutdown/restart/cancel): ").lower()
        if choice in ['shutdown', 'restart', 'cancel', 'exit']:
            if choice == 'cancel':
                continue  # Go back to the prompt
            elif choice == 'exit':
                print("Exiting the program.")
                break  # Exit the loop
            else:
                confirm = input(f"Are you sure you want to {choice} your computer? (y/n): ").lower()
                if confirm == 'y':
                    if choice == 'shutdown':
                        shutdown_system()
                    elif choice == 'restart':
                        restart_system()
                    break  # Exit the loop after the command is executed
                else:
                    print("Action cancelled. Returning to the prompt.")
        else:
            print("Invalid choice. Please enter 'shutdown', 'restart', 'cancel'.")


if __name__ == "__main__":
    main()
