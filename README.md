# NeoGlasses Official - Project Implementation Framework & Guidelines

## Project Structure

> Our project is structured around a **Modular Monolithic Architecture**. This approach is ideal for our Raspberry Pi-based system, where all components operate in a unified environment without relying on external communication. Key characteristics include:

- **Modular Design**: The software is divided into distinct modules, each responsible for a specific functionality (e.g., object detection, text reading). This modularization facilitates independent development and maintenance within a single, cohesive application.

- **Inter-Module Communication**: Modules communicate internally through function calls or internal message queues, enabling efficient data transfer and processing within the system.

- **Centralized Data Management**: A shared data layer is used for inter-module data exchange, ensuring that different modules can access and update shared information seamlessly.

- **Unified Deployment and Execution**: The entire application is compiled and deployed as one executable on the Raspberry Pi. This simplifies deployment processes and enhances performance by utilizing shared resources efficiently.

- **Resource Management**: Given the Raspberry Pi’s limited resources, the architecture is optimized for minimal memory and CPU usage, ensuring that each module operates efficiently within the device's constraints.

- **Event-Driven Design**: The system adopts an event-driven approach, where specific actions or inputs trigger relevant modules to perform tasks, enhancing responsiveness and user interaction.


## Modules Breakdown and Responsibilities

> Our system is composed of several specialized modules, each designed to handle distinct functionalities within the overall application. Below is a breakdown of these modules and their key responsibilities:

1. **Central Control Module (Main Function)**
    - **Responsibility**: Orchestrates overall system operation.
    - **Functionality**: Manages initialization, mode switching, inter-module communication, event handling, and error management.

1. **Camera Input Module**
    - **Responsibility**: Manages the input from dual cameras.
    - **Functionality**: Captures and adjusts images and videos for further processing.

1. **Object Detection Module**
    - Responsibility: Identifies objects within the camera's view.
    - Functionality: Processes images to detect and classify objects, providing relevant information for navigation and interaction.

1. **Text Recognition and Processing Module**
    - **Responsibility**: Handles the recognition and interpretation of text.
    - **Functionality**: Employs Optical Character Recognition (OCR) to convert images of text into machine-readable format.

1. **Navigation and Guidance Module**
    - Responsibility: Assists in spatial navigation.
    - Functionality: Processes data for obstacle detection and provides audio cues for safe navigation.

1. **Text-to-Speech (TTS) Module**
    - **Responsibility**: Converts text to audible speech.
    - **Functionality**: Transforms textual information into speech output for user interaction.

1. **Voice Command Processing Module**
    - **Responsibility**: Processes user’s voice commands.
    - **Functionality**: Captures and interprets audio inputs for system control and mode switching.


## Main Function and Coordinating Module

> The heart of our system is the **Central Control Module**, which acts as the main function and coordinator for the entire application. This module is crucial in tying together the individual components and managing the operational flow. Its key aspects include:

### Central Control Module

- **Responsibility**: Serves as the central hub for system coordination and workflow management.

- **Key Functions**:

    - **Initialization**: Initiates and prepares all modules for operation, ensuring system readiness.

    - **Mode Management**: Manages various operational modes (e.g., object finding, text reading, idle) and switches between them based on user interaction or system triggers.

    - **Inter-Module Communication**: Facilitates data and command transfer between modules, orchestrating cohesive system functionality.

    - **Event Handling**: Responds to events or signals from various modules, coordinating appropriate actions and responses.

    - **Error Handling and Logging**: Monitors the system for potential issues, handling errors gracefully, and maintains logs for system analysis and debugging.


### Mode Triggering and Workflow

- **Operational Modes**:

    - Each mode, such as object finding or text reading, is triggered through specific user commands or predefined conditions.

    - In each mode, relevant modules are activated to process and respond to inputs.


- **Workflow Process**:

    1. **Start-Up**: The system powers up with the Central Control Module initializing all other modules.

    1. **Idle Mode**: By default, the system enters a standby state, awaiting input.

    1. **Mode Activation**: User inputs or environmental triggers prompt the system to switch to the appropriate mode.

    1. **Data Processing**: Activated modules process inputs and perform their designated tasks.

    1. **Output and Interaction**: Results are communicated to the user through audio feedback or other means.

    1. **Mode Transition**: Post-task, the system either reverts to Idle Mode or switches to another operational mode.

## Project Directory Structure
```
project_root/
│
├── main.py                 # Main entry point of the application
│
├── modules/                # Directory for all modular functionalities
│   ├── __init__.py         # Makes modules a Python package
│   │
│   ├── camera.py           # Camera Input Module
│   ├── object_detection.py # Object Detection Module
│   ├── text_recognition.py # Text Recognition and Processing Module
│   ├── text_to_speech.py   # Text-to-Speech Module
│   ├── voice_command.py    # Voice Command Processing Module
│   └── control.py          # Central Control Module
│
├── utilities/              # Utility functions and classes
│   ├── __init__.py         # Makes utilities a Python package
│   └── ...                 # Additional utility scripts
│
├── tests/                  # Unit tests for the modules
│   ├── __init__.py         # Makes tests a Python package
│   └── ...                 # Test scripts for each module
│
├── requirements.txt        # List of project dependencies
│
└── README.md               # Project documentation
```

### Description of Key Components

- `main.py`: This is the entry point of our application. It initializes the system and starts the Central Control Module.

- `modules/`: This directory contains separate Python scripts for each module, encapsulating specific functionalities:
    - `camera.py`: Handles camera operations.
    - `object_detection.py`: Manages object detection logic.
    - `text_recognition.py`: Processes image-based text recognition.
    - `text_to_speech.py`: Converts text to audible speech.
    - `voice_command.py`: Interprets voice commands.
    - `control.py`: Contains the Central Control Module, coordinating other modules.


- `utilities/`: A directory for shared utility functions and classes that are used across different modules.

- `tests/`: Contains unit tests for each module, ensuring code reliability and facilitating maintenance.

- `requirements.txt`: Lists all the Python dependencies required for the project, facilitating easy setup in different environments.

- `README.md`: Documentation for our project, explaining its purpose, setup, and usage.

### Implementation Notes

- Each Python script in the `modules/` directory represents a separate module of our system. These scripts can contain one or more classes or functions, depending on the complexity of the task they handle.

- The `main.py` script should be responsible for initializing and orchestrating the interactions between different modules. It will leverage the **Central Control Module** (`control.py`) for most of its operations.

- It's good practice to include a `README.md` file with clear instructions on how to set up and run our application, along with any other relevant information.

## System Design Concepts and Implementation

### Inter-Module Communication

**Description**

> **Inter-Module Communication** refers to the methods and protocols used by different modules of the system to exchange data and instructions. In our project, this communication is crucial for the coordination of tasks like object detection, text reading, and navigation.

**Implementation**

- **Direct Function Calls**: For simple interactions, one module can directly call functions exposed by another module. For example, `main.py` can invoke methods in `control.py` to switch modes.

- **Message Passing**: Implement a message queue or a similar mechanism within the `control.py` module to facilitate communication between modules. Modules can send and receive messages containing data or commands.

- **Shared Data Structures**: Use shared data structures (like dictionaries, queues) accessible by multiple modules for exchanging data. Ensure thread-safe operations if multiple threads access these structures.


### Centralized Data Management

**Description**

> **Centralized Data Management** involves maintaining a common data repository or structure where multiple modules can store, access, and modify data. This approach ensures data consistency and simplifies data handling across the system.

**Implementation**

- **Shared Database or File**: Use a centralized database or file system (JSON files) where modules read and write data. This could include configuration settings, user preferences, or operational data.

- **Data Access Layer**: Create a data access layer in your `utilities/` directory, providing a unified API for modules to interact with the shared database/file.

- **Synchronization**: Implement synchronization mechanisms to prevent data conflicts, especially in scenarios where multiple modules might try to modify the same data simultaneously.


### Event-Driven Design

**Description**

> **Event-Driven Design** is a paradigm where the flow of the program is determined by events such as user actions, sensor outputs, or message passing. This design is suitable for systems requiring high responsiveness and flexibility.

**Implementation**

- **Event Listeners and Handlers**: Each module can have event listeners that trigger specific handlers when an event occurs. For example, the `camera.py` module can emit an event when a new image is captured, which is then processed by `object_detection.py`.

- **Callback Functions**: Implement callback functions in modules that need to respond to certain events. For instance, a function in `text_to_speech.py` could be registered as a callback for text reading completion events.

- **Asynchronous Processing**: Utilize asynchronous programming (e.g., Python's `asyncio` library) to handle events without blocking the main execution thread, especially important for real-time data processing like camera input or voice commands.


## Streamlined Rapid GitHub Contributions

### Branching Strategy

- **Feature Branches**: Quickly create a branch for each feature or bug fix. For example, `feature/navigation-update` or `bugfix/camera-fix`.

- **Direct Changes on Main Branch**: For minor changes or urgent fixes, allow direct commits to the main branch, but use this sparingly.

### Basic Code Reviews

- **Lightweight Reviews**: Implement quick, informal code reviews for pull requests (PRs), focusing on critical issues.

- **Review for Major Features Only**: Require reviews for major features or significant changes. Small fixes or minor updates can be merged directly after successful testing.

### Pull Requests and Merging

- **Keep PRs Simple**: PRs should be straightforward, addressing specific issues or features to make them easy to understand and merge.

- **Immediate Merging**: Once tested and approved (if required), merge PRs immediately to avoid bottlenecks.

### Coding Standards

- **Essential Standards**: Adhere to basic coding standards necessary for readability and functionality. Avoid strict enforcement that may hinder rapid development.
