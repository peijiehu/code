---
layout: post
title: Ideal vs. Realistic Test Automation
excerpt: ''
categories: [note]
date:   2016-01-15 00:00:00
comments: true
---

## Ideal vs. Realistic Test Automation

The “Test Automation” being discussed here has a broad scope, it contains most levels of tests, including unit test, integration, system test, etc.

Ideally, we want to achieve a structure like this “testing pyramid” below(there are a couple popular ones, this is my favorite, from watirmelon.com – Alister Scott). So, browser automation(Automated GUI Tests) comes last with small number of tests.

![Ideal Software Testing Pyramid]({{ site.url }}/img/testing-pyramid.png)

But for starting a new product with a small team where business changes frequently with a lot of moving parts in product while engineering resource is limited, I prefer do it in this order instead:

1. Small set of Unit Tests for some core logic
2. Automated GUI Tests to cover all critical functionalities
3. Full coverage on Unit Tests

Benefits

This way, we still have basic tests to run during development/commit process, while let browser automation give us confident about how the product behaves to a real user. This can save you a ton of time rewriting specs over and over again as the product is evolving/changing quickly. Additionally, these browser automation tests also serve as documentation of your product.
