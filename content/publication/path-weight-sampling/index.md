---
title: "Path Weight Sampling: Exact Monte Carlo Computation of the Mutual Information between Stochastic Trajectories"
author: ["Manuel Reinhardt", "Gašper Tkačik", "Pieter Rein ten Wolde"]
location: "Physical Review X"
date: 2023-10-26
draft: false
fulltext_link: https://doi.org/10.1103/PhysRevX.13.041017
description: "The information transmission rate of a system can usually be calculated only approximately. A new Monte Carlo simulation scheme makes it possible, for the first time, to do so exactly for a large class of systems."
---

*Manuel Reinhardt, Gašper Tkačik, and Pieter Rein ten Wolde*

Published in [Phys. Rev. X **13**, 041017](https://doi.org/10.1103/PhysRevX.13.041017) (open access [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).

<script type="text/javascript" src="https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js"></script><div class="altmetric-embed" data-badge-type="donut" data-altmetric-id="155802754"></div>

{{< img src="pws_key_image_large960.png" alt="Teaser image" >}}

# Abstract

Most natural and engineered information-processing systems transmit information via signals that vary in time. Computing the information transmission rate or the information encoded in the temporal characteristics of these signals requires the mutual information between the input and output signals as a function of time, i.e., between the input and output trajectories. Yet, this is notoriously difficult because of the high-dimensional nature of the trajectory space, and all existing techniques require approximations. We present an exact Monte Carlo technique called path weight sampling (PWS) that, for the first time, makes it possible to compute the mutual information between input and output trajectories for any stochastic system that is described by a master equation. The principal idea is to use the master equation to evaluate the exact conditional probability of an individual output trajectory for a given input trajectory and average this via Monte Carlo sampling in trajectory space to obtain the mutual information. We present three variants of PWS, which all generate the trajectories using the standard stochastic simulation algorithm. While direct PWS is a brute-force method, Rosenbluth-Rosenbluth PWS exploits the analogy between signal trajectory sampling and polymer sampling, and thermodynamic integration PWS is based on a reversible work calculation in trajectory space. PWS also makes it possible to compute the mutual information between input and output trajectories for systems with hidden internal states as well as systems with feedback from output to input. Applying PWS to the bacterial chemotaxis system, consisting of 182 coupled chemical reactions, demonstrates not only that the scheme is highly efficient but also that the number of receptor clusters is much smaller than hitherto believed, while their size is much larger.

[Read more...](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.13.041017)