# Requirements Overview

## 1. Document Outline
This document gives the detailed specifications for the new toolkit. It is organized as follows:
- [Section 2: Functional Requirements](#2-functional-Requirements)
    - Each objective gives a desired behavior for the system. These requirements are organized by priority.
    - In order for the new system to be considered successful, all high and medium priority, as well as documentation, requirements must be met.
  - Use it to keep track of the requirements as you meet them. It will be used by Mentors to check progress and approve Pull Requests
- [Section 3: Non-Functional Requirements](#3-non-functional-requirements)
  - This section is organized by category. Each objective specifies a technical requirement or constraint on the overall characteristics of the system. Each objective is measurable.

## 2. Functional Requirements

To simulate the 12 agile development principles, and meeting customer demands as soon as possible, you will perform [iterative, incremental delivery](https://www.rebelscrum.site/post/incremental-delivery-and-the-principles-of-the-agile-manifesto#:~:text=What%20is%20iterative%2C%20incremental%20delivery).

- You will release Cyber Capability Capstone v0.1 when you complete the **High Priority Requirements**
- You will release Cyber Capability Capstone v0.2 when you complete the **Medium Priority Requirements**
- You will release Cyber Capability Capstone v1.0 when you complete the **Documentation Requirements**
- These releases will be performed using the [GitHub Releases feature](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
    - You can have as much fun with this as you want (optional)! Make GitHub Kanban boards, Milestones for the Releases, Sprints, etc
    - Mentors are more than happy to get you setup with those
- Each of these releases will be developed on a development branch, **not `master` or `main`**
    - In between these official Releases, you will commit to your repo each time you implement a specific Requirement
    - When you are ready for a Release, you will create a Pull Request, attempting to merge your work into your `master` branch and assign a Mentor to review it
    - If its satisfactory, the merge will be allowed and you may then create the Release
    - More likely than not however, it will be returned with comments on required improvements

The below sections will be used by Mentors when checking what requirements you've met for regular checkups or PR reviews.

### High Priority Requirements (v0.1)
- [ ] **H.1:** The framework shall be developed in a Git repository with appropriate documentation and installation guidance. For versions 0.1 & 0.2, code comments will suffice.
   - [Git](./resources/course/DevOps/3-Git.md)
   - [Documentation](./resources/course/DevOps/9-Documentation.md)
- [ ] **H.2:** The system shall compile with no warnings and run with no memory leaks
   - [Valgrind and Baby DevOps](./resources/course/DevOps/7-ValgrindandBabyDevOps.md)
- [ ] **H.3:** The framework shall allow for on-demand customization by the operator to set capabilities at compile time using a Python script which leverages compile-time Macro values
   - [Starter Code](./resources/course/DevOps/11-Starter.md)
- [ ] **H.4:** The system shall implement a system validator (*stage 1*) that will gather information about the kernel, operating system, and users. Check out [src/README.md](./src/README.md) for details.
   - [Profiler](./resources/course/Backdoor_Basics/7-Profiler.md)
- [ ] **H.5:** The system shall allow reverse shell access to remote hosts through a backdoor (*stage 2*) that will listen for port knocks and return a reverse shell when it receives them. Check out [src/README.md](./src/README.md) for details.
   - [Reverse Shell](./resources/course/Advanced_Payloads/2-ReverseShell.md)
   - [Activation and Connecting to Shells](./resources/course/Advanced_Payloads/1-ActivationandConnectingtoShells.md)
- [ ] **H.6:** The system shall have the capability to add execution guardrails based on Target IPv4 Address, Hostname, Language configured on the system, and a desired Date Range.
   - [Execution Guardrails and Validators](./resources/course/Backdoor_Basics/0-ExecutionGuardrailsandValidators.md)
- [ ] **H.7:** The system shall have the ability to daemonize using fork and exec
   - [ForkExec and Processes](./resources/course/Linux_Development_and_Portability/9-ForkExecandProcesses.md)
   - [Daemonize](./resources/course/Execution/0-Daemonize.md)

### Medium Priority Requirements (v0.2)
- [ ] **M.1:** Operators should be able to specify at compile time if the binaries are stripped
    - [Stripped Binaries](./resources/course/Linux_Development_and_Portability/7-StrippedBinaries.md)
- [ ] **M.2:** Operators should be able to specify at compile time if the binaries are 32 bit or 64 bit
    - [Architecture Portability](./resources/course/Linux_Development_and_Portability/3-ArchitecturePortability.md)
- [ ] **M.3:** Operators should be able to specify at compile time if the binaries are statically or dynamically linked
    -  [Linking and Loading](./resources/course/Linux_Development_and_Portability/2-LinkingandLoading.md)
    -  [Dynamic Compilation](./resources/course/Linux_Development_and_Portability/4-DynamicCompilation.md)
    -  [Static Compilation](./resources/course/Linux_Development_and_Portability/6-StaticCompilation.md)
- [ ] **M.4:** The compiler script shall save all information about each implant to a log
   - [Python Build](./resources/course/DevOps/8-PythonBuild.md)
- [ ] **M.5:** The system shall have a verbose debug mode and zero print statements in its operational mode
   - [Error Handling](./resources/course/DevOps/4-ErrorHandling.md)
   - [Debugging](./resources/course/DevOps/6-Debugging.md)
- [ ] **M.6:** The system shall share no code with any existing internal implants or well-known open source tools
- [ ] **M.7:** The system shall have the ability to automatically uninstall itself once outside of date execution guardrails
   - [Uninstall](./resources/course/Backdoor_Basics/6-Uninstall.md)
- [ ] **M.8:** The implant shall not have any unique strings in the binary
   - [EncodingEncryption](./resources/course/Customization/5-EncodingEncryption.md)
- [ ] **M.9:** If a reverse connection fails to connect, the implant will do an exponential backoff, doubling the length of time slept before attempted connections each time

### Documentation Requirements (v1.0)
- [ ] **D.1:** Overall, the developer shall provide documentation that explains how to:
   - Install the Framework
   - Compile Implant
   - Operate the implant
   - Tips on troubleshooting or any bugs
- [ ] **D.2:** The developer shall fill out the [src/README.md](./src/README.md) file as they go with Documentation on the Purpose, Data Types, Methods, and Operating Tips for
   - The `buildAndConfig` folder
   - The `validator` folder
   - The `backdoor` folder
- [ ] **D.3:** All source files shall have an acceptable [File Header Comment](http://syque.com/cstyle/ch4.4.htm) 
   - At minimum it must contain the file's description, name, author, last modify date
- [ ] **D.4:** Throughout the source code, appropriate code commenting shall be applied
   - Method descriptions must be provided in header files with the method declarations
   - Struct descriptions must be provided in header files with the struct definitions
   - All non-intuitive Macros' purposes must be described

---
## 3. Non-Functional Requirements

### 3.1 Reliability
The system shall be completely operational at all times.

### 3.2 Usability
- An operator should be able to use the system in his job after 2 hours of training.
- A developer should be able to add a new function to the implant in under an hour. 
- The installation script should set everything up automatically

### 3.3 Performance
The system should be reasonably responsive, accounting for network latency.

### 3.4 Security
The system shall have no vulnerabilities that would allow exploitation on it by the target (no buffer overflows, etc).

### 3.5 Supportability
The system should be able to accommodate new products and product lines without major re-engineering (**i.e. Make it Modular**).

### 3.6 Purchased Components
None.

### 3.7 Interfaces
The implant build tools must provide a CLI for operators to specify different compile-time options.
