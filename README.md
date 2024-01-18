# NeoGlasses Official - Project Implementation Framework & Guidelines

## Project Structure: Microkernel Architecture

> Our project adopts a Microkernel Architecture. This design is well-suited for our Raspberry Pi-based system, focusing on a minimal core (the microkernel) that facilitates communication and coordination among various independent modules. This architecture is key in a system that prioritizes modularity and flexibility, especially when not relying on external network communication. The main features of this architecture are:


- **Microkernel as Central Controller**: The Central Control Module acts as the microkernel, handling essential system operations. It initializes modules, manages mode switching, and serves as the primary communication hub.

- **Modular Plug-In Design**: Each major functionality (like object detection, text reading) is encapsulated within distinct modules. These modules, akin to plug-ins, interact with the microkernel through well-defined interfaces, allowing them to be developed and maintained independently.

- **Indirect Inter-Module Communication**: Instead of direct communication between modules, all interactions occur indirectly via the microkernel. This design enhances system stability and simplifies inter-module communication.

- **Efficient Resource Management**: The microkernel is designed to be lightweight and resource-efficient, crucial for the Raspberry Pi’s limited resources. It ensures optimal operation of each module within the device's constraints.

- **Event-Driven Mechanism**: The system employs an event-driven model where modules can emit events or signals to the microkernel. The microkernel, in turn, processes these signals and coordinates the appropriate actions across other modules.

- **Scalability and Flexibility**: New functionalities can be seamlessly integrated as separate modules, and existing modules can be updated independently. This flexibility is a core strength of the Microkernel Architecture, allowing for easy adaptation and evolution of the system.

## Modules Breakdown and Responsibilities

> In our system, designed around a Microkernel Architecture, we have a central control module (the microkernel) and several specialized modules (akin to plug-ins). Each module is dedicated to specific functionalities within the application. Here's a breakdown of these modules and their key responsibilities:

1. **Central Control Module (Microkernel)**
    - **Responsibility**: Acts as the core of the system, orchestrating overall operation and communication.
    - **Functionality**: Manages system initialization, coordinates inter-module communication, handles mode switching, processes events and signals from other modules, and oversees error management.

1. **Camera Input Module (Plug-In)**
    - **Responsibility**: Manages the input from dual cameras.
    - **Functionality**: Captures images and videos, providing data to the Central Control Module for further processing.

1. **Object Detection Module (Plug-In)**
    - **Responsibility**: Identifies objects within the camera's view.
    - **Functionality**: Processes images from the Camera Input Module to detect and classify objects, then communicates findings to the Central Control Module.

1. **Text Recognition and Processing Module (Plug-In)**
    - **Responsibility**: Handles the recognition and interpretation of text from images.
    - **Functionality**: Utilizes Optical Character Recognition (OCR) to convert images of text into machine-readable format, and reports results to the Central Control Module.

1. **Text-to-Speech (TTS) Module (Plug-In)**
    - **Responsibility**: Converts text data into audible speech.
    - **Functionality**: Receives textual information from the Central Control Module and transforms it into speech output for user interaction.

1. **Voice Command Processing Module (Plug-In)**
    - **Responsibility**: Interprets user’s voice commands.
    - **Functionality**: Captures and processes audio inputs, then sends interpreted commands to the Central Control Module for appropriate action.

## Main Function and Coordinating Module

> At the core of our system is the Central Control Module, functioning as the microkernel in our Microkernel Architecture. This module is pivotal in orchestrating the operations of the plug-in modules and managing the overall workflow. It ensures seamless interaction between different components and maintains the integrity of the system's operation. The critical aspects of this module are as follows:


### Central Control Module (Microkernel)

- **Responsibility**: Acts as the core controller and coordinator for the entire system.

- **Key Functions**:

    - **Initialization**: Starts and configures all plug-in modules, ensuring they are ready for operation. It establishes the foundational state of the system.

    - **Operational Mode Management**: Oversees different operational modes (such as object finding, text reading, idle, etc.). It activates or deactivates relevant plug-in modules based on the current mode.

    - **Core Communication Hub**: Acts as the central point for all inter-module communication. Plug-in modules send their data and signals to the microkernel, which then decides the subsequent actions and relays commands back to the appropriate modules.

    - **Event and Signal Processing**: Listens to and processes events or signals emitted by plug-in modules. Based on these inputs, it coordinates the appropriate workflow and module interactions.

    - **Error Handling and System Stability**: Maintains system stability by handling errors and exceptions that occur within plug-in modules. It ensures that issues in one module do not compromise the overall system functionality.

### Mode Triggering and Workflow
> In our system, which employs a Microkernel Architecture, the Central Control Module (Microkernel) effectively manages various operational modes and oversees the system's workflow. This approach ensures a streamlined and efficient operation, with each mode corresponding to specific user needs and scenarios

- **Operational Modes**:

    - **User-Driven and Condition-Based Triggers**:

        - Different operational modes like object finding, text reading, or idle are activated through user commands or specific environmental conditions detected by the system.

        - The Central Control Module (Microkernel) interprets these triggers and activates the corresponding plug-in modules.

    - **Modular Activation**:
        - In response to a mode change, the Microkernel selectively activates or deactivates the necessary plug-in modules. This modular activation is crucial for resource efficiency and task specificity.

- **Workflow Process**:

    1. **System Start-Up**: Upon powering up, the Microkernel initializes and configures all plug-in modules, preparing the system for operation.


    1. **Default Idle Mode**: The system, by default, enters an idle state where it consumes minimal resources while remaining responsive to user input or significant environmental changes.


    1. **Mode Activation**: When a user command is received or a specific condition is met, the Microkernel assesses and transitions the system to the appropriate operational mode.

    1. **Data Processing and Task Execution**: The activated plug-in modules process the incoming data or perform tasks as required by the current mode. For example, in text reading mode, the Text Recognition Module processes the image data to extract and interpret text.

    1. **Output Generation and User Interaction**: The results from the active modules are collated by the Microkernel and conveyed to the user through audio feedback.

    1. **Transition Between Modes**: Upon completing the tasks of the current mode, the Microkernel either returns the system to Idle Mode or transitions to another mode based on new inputs or conditions

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

- **Microkernel-Centric Structure**

    - The `modules/` directory contains Python scripts representing plug-in modules of the system. Each script encapsulates specific functionalities like camera input handling, object detection, or voice command processing.

    - These scripts are designed to interact with the Central Control Module (Microkernel), located in the `control.py` file. They provide specific services and process information as requested by the Microkernel.

- **Central Control Module (`control.py`):**

    - This script acts as the Microkernel of our system. It is responsible for initializing the system, managing the lifecycle of plug-in modules, handling inter-module communication, and coordinating overall system operations.

    - The Microkernel maintains a high-level control over the system, delegating specific tasks to plug-in modules and ensuring seamless cooperation between them.

- **`main.py` as System Initiator:**

    - The main.py file serves as the entry point of the application. Its primary role is to initialize the Microkernel and kickstart the system's operations.
    
    - It calls the initialization function in the Central Control Module, which in turn prepares the system by setting up the plug-in modules and readying them for operation.


- It's good practice to include a `README.md` file with clear instructions on how to set up and run our application, along with any other relevant information.

## System Design Concepts and Implementation

### Inter-Module Communication

**Description**

> In our Microkernel Architecture, **Inter-Module Communication** is a pivotal element that enables the central control module (Microkernel) and the various plug-in modules to exchange data and commands effectively. This communication strategy is vital for orchestrating complex tasks like object detection, text reading, and voice command processing in our system.

**Implementation**

- **Centralized Communication Through Microkernel**: Instead of direct communication between modules, all interactions occur via the Microkernel. This approach aligns with the Microkernel Architecture, where the central control module acts as the mediator and manager of communication.

- **Event and Signal Handling**: The Microkernel listens for events or signals emitted by plug-in modules. Upon receiving an event, it processes the signal and orchestrates the actions of other relevant modules.

- **Message Queue (Optional)**: If needed, a message queue can be integrated within the Microkernel for managing asynchronous communication and handling multiple requests efficiently.

- **Thread-Safe Data Handling**: When shared data structures are necessary, the Microkernel manages access to these resources, ensuring thread-safe operations to maintain data integrity across the system.

### Centralized Data Management

**Description**

> In the context of Microkernel Architecture, **Centralized Data Management** is critical for managing and maintaining data consistency across various plug-in modules. The Microkernel acts as the intermediary for data access and modification, ensuring a unified and coherent data flow.


**Implementation**

- **Microkernel-Managed Data Access**: The Microkernel coordinates access to a centralized data repository, like a database or file system (JSON File). It handles requests from plug-in modules to read or write data, ensuring consistent and synchronized data management.

- **Focused Data Access Layer**:
A specific data access layer within the Microkernel provides a streamlined API for data operations, reducing direct data handling complexity in plug-in modules.


- **Controlled Synchronization**: The Microkernel manages data synchronization, addressing potential conflicts in data access or modification by multiple modules, thereby maintaining data integrity.

### Event-Driven Design

**Description**

> **Event-Driven Design** plays a key role in orchestrating interactions between the central control module (Microkernel) and various plug-in modules. This approach enhances system responsiveness and adaptability, with the flow being directed by events like user inputs, sensor data, or internal notifications.

**Implementation**

- **Centralized Event Management**: The Microkernel serves as the central point for managing events. It listens to events emitted by plug-in modules and orchestrates the appropriate responses.

- **Event Dispatching**: Upon receiving an event from a plug-in module (e.g., a new image captured by `camera.py`), the Microkernel dispatches the event to relevant modules (such as `object_detection.py`) for processing.

- **Microkernel Callbacks**: Implement callback mechanisms within the Microkernel. When a plug-in module completes a task, it notifies the Microkernel, which then triggers the next step in the process.

- **Efficient Asynchronous Handling**: The Microkernel manages asynchronous events using techniques like Python's asyncio, ensuring that event processing does not block the system's main operational flow.

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
