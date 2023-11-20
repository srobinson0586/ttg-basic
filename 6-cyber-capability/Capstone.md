# Capstone Overview

## Project Introduction

### Purpose of Section
This is a Project Specification section for a custom Linux implant and accompanying toolset that will share no code with any pre-existing capabilities. 

### Project Summary
- Project Name: Cyber Capability Capstone
- Project Manager: N7 Developer TRAINO
- Responsible Users: **STUDENT NAME HERE**, Customer

### Background
Ropping Goat is an organization which conducts offensive operations in support of Country Blue, with a focus on persistent access and on-time delivery of effects. 

While our existing toolkits are very sophisticated, we are looking for a new toolset to be added to our library that will not require use of advanced techniques to bypass anti-virus and cloud scanning defenses. Operators have been detected prior to install recently by these automated defenses, and we cannot justify the use of our advanced crypting and packing techniques for lower priority targets.

Anticipating this need, we are building out a set of unattributable, low-equity, fully custom implants that will be able to be deployed when and where needed. 

### Project Scope
The scope of this project is a minimal CNO toolset for Linux systems written in the C programming language that can provide persistent access to a target. This is a green field project with minimal sample code.

Relative to the [MITRE ATT&CK Framework](https://attack.mitre.org/), only the following *Tactics* will be employed in this project:
- Resource Development
- Persistence
- Collection
- Exfiltration

As alluded to above, obtaining code execution is not part of this project. You can assume that operators are able to run your implant as `root`. The system will not be responsible for managing implants or any C2. The original course has students implement most of the *Tactics*, but we will only worry about the basics here.

### System Purpose

#### Users
Those who will primarily benefit from the new system and those who will be affected by the new system include:
- Operators
    - Upon implementation of the new system, operators will be able to have a non-attributable basic implant that can be used in their day to day duties which will not risk the loss of advanced bypass techniques. Documentation for their day-to-day activities will be key.

- Information Technology Department
    - This department will be responsible for setting up the system for operators and running the command and control. They will rely on your install scripts and documentation.

- Developers
    - All code produced during this project will be passed off to internal developers who will continue work on the codebase. They will rely on your documentation.

#### Location
Once installed, the toolset will be available to any operator on our local network.

#### Responsibilities
The primary responsibilities of the new system:
- Provide operators access to remote systems
- Customize implant based on required capabilities
- Minimize signature of implant
- Other desired features of the new system:
    - Do not cause any errors or extraneous logs to be created on target hosts

#### Need
This system is needed in order to service the increase in demand for non-attributable, low equity access to low-priority systems.

## Project Context Model

### Goal Statement
The goal of the system is to allow operators to explicitly define the capabilities, execution guardrails, and functionality at compile time and be provided an implant with minimal signature to be used for access.

### Context
1. Operator requests implant providing following information
   1. Architecture
   2. Whether the binary should be stripped
   3. Whether it should be Statically or Dynamically linked
   4. Execution guardrails
      1. Target IP
      2. Target Hostname
      3. Target Language
      4. Target Date Range
2. Builder runs build script which allows dynamic compile-time options
   1. Passes request parameters into compilation script
   2. Script runs automatically and uses #define to specify what is included in executable
   3. Implant is generated, parameters logged
3. Operator is given custom implant
4. Operator executes implant on target using advanced access technique
5. Implant establishes persistence (if desired) and opens up a shell
6. Operator accesses shell and conducts actions on objectives

### Context Diagram
If desired, create your own flow chart or UML Diagram here. It could help you plan out this relatively big project. Diagraming how all the general components of your software product *should* work together will go a **long way** in *Software Engineering*.

The importance of the planning phase in the development of a software product **cannot be stressed enough** and will save you considerable amounts of time and headaches. This concept is expressed more formally in industry as the "Software Design" phase of the [*Software Development Life Cycle*](https://www.harness.io/blog/software-development-life-cycle).

Some optional resources on Software Development/ Software Architecture:
- [Intro to SDLC](https://www.youtube.com/watch?v=Fi3_BjVzpqk)
- [draw.io](https://www.drawio.com/) is a *Free* online Diagramming tool that could help you create:
  - System state diagrams (*[2.2 Context](#22-context) but graphic*)
  - Software architecture designs (*model how different components in your design will interoperate*)
