---
layout: post
title: Testing System Design
excerpt: ''
categories: [note]
date:   2017-06-06 00:00:00
comments: true
---

## Testing System Design

### Principles

We want a system in which:

- Code is tested as single units of work
- We avoid testing the same code twice
- We avoid testing 3rd party code
- External systems are not required or are trivial to orchestrate
- Production code is free of test code

One of the most common and most prevalent solutions to this is the use of Dependency Injection together with Mock Objects.

### Isolation

To ensure tests are isolated and idempotent, we have the following options:

1. Seed data and/or initialize state needed for every test, a test can generate data or change state during execution, but it won't affect the next run since it always use the initial seed data or state.
2. Seed data in setup, revert changes back at the end of each test (eg. update data to its original state, delete newly created entry), or revert during teardown.

The goal is that changing the order in which tests are run or re-running the same tests multiple times should not affect the outcome.

### Automated Tests for Asynchronous Processes

If you are finding the need for async testing in your unit tests, you’re probably doing something wrong and need to redesign your code to decouple these concerns.
There are generally two approaches to testing asynchronous behaviour:

1. Remove the asynchronous behaviour
2. Poll until you have the desired state
