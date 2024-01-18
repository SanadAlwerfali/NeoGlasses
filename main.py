# Main entry point of the application
from modules.control import CentralControlModule


def main():
    # Create an instance of the Central Control Module
    central_control = CentralControlModule()

    # Start the main loop of the central control
    try:
        central_control.main_loop()
    except KeyboardInterrupt:
        # Gracefully handle any cleanup here if the program is interrupted
        pass
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")
    finally:
        # Any final cleanup code can be placed here
        pass

if __name__ == "__main__":
    main()
