# Describe Code Testing Fundamentals

[Back to OVERVIEW](../README.md)

Read through the following sections and answer the questions in the [Questions](#questions) section.

## Testing Philosophy and Design

This organization's testing philosophy includes producing code that is unit tested with appropriate integration tests and deployed to a CI/CD pipeline/framework. CI/CD is an acronym for *continuous integration and continuous delivery/continuous deployment*.

A CI/CD pipeline will run changes in our code in as many software environments or configurations as necessary to meet the reliability requirements of our clients. Developers are typically responsible for unit code coverage and specifications of integration tests. However DevOps staff may also assist in such endeavors. DevOps staff are typically responsible for the implementation and maintenance of the pipeline framework.

Watch the [CI/CD in 5 Minutes](https://www.youtube.com/watch?v=42UP1fxi2SY) for a more in-depth explanation.


## Unit Testing Versus Integration Testing

**Unit testing** is a software testing method by which individual units of source code—sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures—are tested to determine whether they are fit for use.  It is a standard step in development and implementation approaches such as Agile.

**Integration testing** is conducted to evaluate the compliance of a system or component with specified functional requirements.  In the context of our organizational work, integration tests are often used to test the results of operating system and API calls, or communication between multiple pieces of software.  Typically, a successful integration test produces output that matches expected results determined statically (predetermined) or dynamically (by calling other reference tools for output).

A very wise scholar once wrote a renowned commentary on testing (among other things) and avoiding overly complex testing. It might be worth a read at [grugbrain.dev](https://grugbrain.dev/#grug-on-testing), as well as this informative video: [Unit & Integration Testing COMPARED](https://www.youtube.com/watch?v=pf6Zhm-PDfQ).


## Modular versus Monolithic Design

**Monolithic**: a monolithic framework typically provides a tightly coupled codebase that makes a lot of assumptions about how the code interacts with each other. The codebase is developed, deployed, and scaled as a single component.

**Modular**: as you can guess a modular framework is more minimal and only provides the bare-bones functionality and structure for your application. Each component generally only has one "responsibility". The code is more loosely coupled where each part of code communicates in a more or less standard interface such as APIs and Message Brokers.

Check out the [Monolithic vs Microservice Architecture](https://www.youtube.com/watch?v=NdeTGlZ__Do) YouTube video for a more in depth explanation.


## Continuous Integration

**Continuous integration** is a DevOps software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.  Our organization's testing philosophy demands continuous incorporation of new integration tests on additional code and continuous monitoring of test results in the CI/CD pipeline.

## Questions

Answer the questions below according to the following scenario:
> You are part of the Development Team in charge of a new [Cobalt Strike](https://www.cobaltstrike.com/product/features) feature that allows users to inject a Beacon into a target computer's System Memory and execute it. You've been developing this new feature independently of the rest of the Cobalt Strike Framework. All the individual components of the new feature have been tested already, but you need to see how it will work with the rest of the Cobalt Strike Framework.

1. What testing methodology will you be using to write the required tests?
    ```
    ANSWER:
    ```

2. Would you say that your team has adopted a *Monolithic* Design or a *Modular* design?
    ```
    ANSWER: 
    ```

3. What part of the CI/CD pipeline would your tests be a part of (CI or CD)?
    ```
    ANSWER:
    ```

[Back to OVERVIEW](../README.md)