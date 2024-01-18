# Main entry point of the application
from modules.control import CentralControlModule

def main():
    # Create an instance of the Central Control Module (Microkernel)
    central_control = CentralControlModule()

    # Start the main loop of the central control
    # This loop will keep the application running and responsive to module interactions
    try:
        central_control.main_loop()
    except KeyboardInterrupt:
        # Graceful shutdown if the program is interrupted (e.g., Ctrl+C)
        print("Shutting down the system...")
        # Here you can add any cleanup or shutdown procedures
    except Exception as e:
        # Handle any unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        # Any final cleanup code can be placed here
        # This is important for releasing resources like file handles or network connections
        pass

if __name__ == "__main__":
    main()
