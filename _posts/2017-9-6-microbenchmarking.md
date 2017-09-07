---
layout: post
title: Shared Notes on Microbenchmarking
excerpt: ''
categories: [note]
date:   2017-09-06 22:17:00
comments: true
---

## Good read on Microbenchmarking
Disclaimer: I didn't write these, mostly just sharing from http://scalameter.github.io/home/gettingstarted/0.7/

### Tradeoff: Optimization vs Complexity & Portability
Small performance optimizations can make software more fragile and complex, and they also depend on many assumptions.

That said, when do you want to write a microbenchmark? Here are some examples:

- optimize a known and well-established bottleneck in an application
- compare several implementation alternatives, e.g. several algorithms
- verify that an optimization is an optimization at all
- have a performance regression test for a particular piece of code

### Typical Unit Test vs Performance Regression Test

First, microbenchmark running times are not deterministic. For example, a run A may have the running time 15ms and a subsequent run B the running time 16ms. Does that mean that the run B is a performance regression? Probably not. The two alternative microbenchmarks have to be run more than once and a statistical analysis has to be applied to decide if one of the alternatives is a regression.

Second, the running time of a certain benchmark is not reproducible on different machines, JVM versions or operating systems. This means that a tester cannot write a test where the running time is hardcoded into the test itself. Instead, preliminary benchmarks have to be executed on a particular machine on a particular operating system with a particular JVM version. The execution times of these preliminary benchmarks are then persisted for later comparison.

These two crucial differences between normal regression tests and performance regression tests are the reason why ScalaMeter exists – to allow you to write and run performance tests in a reliable manner, where the performance regressions can be detected deterministically and running times reproduced under the same conditions.
