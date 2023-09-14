# Demonstrate skill in writing and evaluating software tests

## Purpose

This competency will get you familiar with writing tests for existing software that you didn't write yourself. Testing target software for bugs is a very important responsibility of a CNO Developer. Obviously the target software isn't usually interpreted, but this will help get you into that h4ck3r mindset.

*Aside*
> You can imagine the real-life application of this competency by replacing `spec.md` with [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616#section-4.4) (HTTP/1.1 Specification), and the `expression` python module with a target Webserver's *transfer encoding* implementation.
> 
> This is how Portswigger's `@albinowax` [successfully weaponized HTTP DeSync attacks](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) to win over $70,000 in bounties in a couple of months.

## Context

This directory contains a Python package (in the `expression/` subdirectory)
intended to parse and evaluate arithmetic expressions.

The expression format specification is in [`spec.md`](./spec.md).

You don't need to modify (or even look at) the contents of the `expression`
package. It only provides the functionality you will be testing.

Your job will be to add more test functions to
[`test_expression.py`](./test_expression.py) to find the bugs in the package.

You will need to test all functionality described in the specification,
including that `expression` raises the correct types of errors (with the
correct attribute information).

## Instructions

1. Read and understand the expression format specification in [`spec.md`](./spec.md).
2. Write more `test_*` functions in [`test_expression.py`](./test_expression.py) to test all the functionality described in the spec.
   1. Run `$ pytest` in this directory to have `pytest` run all your test functions.
3. Succinctly document in [`bugs.txt`](./bugs.txt) all the bugs you found. There are 10 distinct bugs with the program. You will be publicly praised if you uncover unintended bugs in the program!
