---
title: "Computing the Information Flow Through Complex Systems"
date: 2022-02-07
location: "internal AMOLF “Klein Colloquium”"
draft: false
description: "Oral presentation held at internal AMOLF “Klein Colloquium”"
---

[Download the Presentation as PDF](/2022-klein-colloquium.pdf)

{{< slide src="slides/Klein Colloquium.001.png" alt="slide1" >}}

Information Processing systems are all around us, ranging from
- electronic devices,
- optical systems,
- neuronal networks to
- biological systems.

{{< slide src="slides/Klein Colloquium.002.png" alt="slide2" >}}

Quantifying information flow is vital for
understanding or improving these systems.

Nearly 70 years ago, Claude Shannon realized that information can be precisely quantified mathematically. 

{{< slide src="slides/Klein Colloquium.003.png" alt="slide3" >}}

The central performance measure for information processing systems is the *information transmission rate*, which quantifies how many bits per second the system transmits. Yet, up till now this quantity could only be computed approximately.

{{< slide src="slides/Klein Colloquium.004.png" alt="slide4" >}}

We have developed a Monte Carlo simulation scheme that makes it possible, for the first time, to compute the information transmission rate exactly for a large class of systems. Our scheme, called Path Weight Sampling (PWS), can not only be applied to compute the information transmission rate for theoretical models of these systems, but also makes it possible to estimate the rate from experimental observations using effective models (such as Hidden Markov Models) obtained from empirical data. 

{{< slide src="slides/Klein Colloquium.005.png" alt="slide5" >}}

PWS is made efficient by establishing connections between quantities from information theory and statistical physics, such as path probabilities and partition functions, making it possible to leverage techniques from soft condensed matter physics, like transition path sampling and polymer simulation algorithms.

{{< slide src="slides/Klein Colloquium.006.png" alt="slide6" >}}
{{< slide src="slides/Klein Colloquium.007.png" alt="slide7" >}}

We demonstrate the practical utility of our method by computing the information transmission rate for a complex real-world system: the bacterial chemotaxis network. Applying PWS to this network we demonstrate not only that the simulation scheme is
highly efficient, but also that the appropriate measure for quantifying information transmission via
time-varying signals is indeed the information transmission rate. Other information measures such as the widely used *instantaneous mutual information* cannot correctly predict the input signal that optimizes the information flow for this system.

{{< slide src="slides/Klein Colloquium.008.png" alt="slide8" >}}

{{< slide src="slides/Klein Colloquium.009.png" alt="slide9" >}}

I would like to thank everyone in my research group as well as our collaborator
Gašper Tkačik at IST Austria.

{{< slide src="slides/Klein Colloquium.010.png" alt="slide10" >}}
