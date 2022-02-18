---
title: "Presentation: Computing the Information Flow Through Complex Systems"
date: 2022-02-07
categories: 
  - presentation
draft: false
description: "Oral presentation held at internal AMOLF “Klein Colloquium”"
---

**Title:** Computing the Information Flow Through Complex Systems<br>
**Authors:** *Manuel Reinhardt, Gašper Tkačik, and Pieter Rein ten Wolde*

[Download the Presentation as PDF](/2022-klein-colloquium.pdf)

# Summary

Information Processing systems are all around us, ranging from
- electronic devices,
- optical systems,
- neuronal networks to
- biological systems.

Quantifying information flow is vital for
understanding or improving these systems.

Nearly 70 years ago, Claude Shannon realized that information can be precisely quantified mathematically. The central performance measure for information processing systems is the *information transmission rate*, which quantifies how many bits per second the system transmits. Yet, up till now this quantity could only be computed approximately. 

We have developed a Monte Carlo simulation scheme that makes it possible, for the first time, to compute the information transmission rate exactly for a large class of systems. Our scheme, called Path Weight Sampling (PWS), can not only be applied to compute the information transmission rate for theoretical models of these systems, but also makes it possible to estimate the rate from experimental observations using effective models (such as Hidden Markov Models) obtained from empirical data. PWS is made efficient by establishing connections between quantities from information theory and statistical physics, such as path probabilities and partition functions, making it possible to leverage techniques from soft condensed matter physics, like transition path sampling and polymer simulation algorithms.

We demonstrate the practical utility of our method by computing the information transmission rate for a complex real-world system: the bacterial chemotaxis network. Applying PWS to this network we demonstrate not only that the simulation scheme is
highly efficient, but also that the appropriate measure for quantifying information transmission via
time-varying signals is indeed the information transmission rate. Other information measures such as the widely used *instantaneous mutual information* cannot correctly predict the input signal that optimizes the information flow for this system.

<iframe src="https://www.icloud.com/keynote/00dqS5MqZbpwgWAyT4Kob69eQ?embed=true" width="640" height="500" frameborder="0" allowfullscreen="1" referrer="no-referrer"></iframe>