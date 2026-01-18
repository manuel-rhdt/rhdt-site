---
title: "PhD Thesis: Quantifying the Flow of Information"
author: ["Manuel Reinhardt"]
location: "Vrije Universiteit Amsterdam"
date: 2025-06-13
fulltext_link: https://ir.amolf.nl/pub/11167
draft: false
description: "I successfully defended my PhD thesis."
---

I'm excited to announce that I successfully defended my PhD thesis titled **"Quantifying the Flow of Information"** on June 13, 2025, at Vrije Universiteit Amsterdam.

## What the Thesis is About

Understanding how information flows through biological and engineered systems is fundamental to analyzing and improving them. My thesis introduces **Path Weight Sampling (PWS)**, a novel computational framework that makes it possible to exactly calculate how much information time-varying signals carry.

The key challenge is that most systems process signals that change over time, and quantifying information transmission in these dynamic signals is notoriously difficult. The trajectory space—all possible ways a signal can evolve—grows exponentially, making conventional approaches computationally intractable. This is known as the "curse of dimensionality."

## The Solution: Path Weight Sampling

PWS is the first exact Monte Carlo technique for computing mutual information between stochastic trajectories. The core innovation is using master equations (mathematical descriptions of stochastic dynamics) to compute exact conditional probabilities for entire signal trajectories, then averaging these using smart Monte Carlo sampling techniques.

I developed three variants of PWS:
- **Direct PWS**: A brute-force Monte Carlo approach
- **RR-PWS**: Uses bootstrap particle filters inspired by polymer physics
- **TI-PWS**: Employs thermodynamic integration with MCMC sampling

## Real-World Application: Bacterial Chemotaxis

To demonstrate PWS in action, I applied it to bacterial chemotaxis—how *E. coli* bacteria sense and navigate chemical gradients. The system is complex, involving 182 coupled stochastic reactions operating across multiple timescales.

The analysis revealed a surprising finding: the standard literature model couldn't explain data from recent experiments. The results suggest that *E. coli* cells have **fewer receptor clusters** (~4-6 instead of 8-10) but with **larger cluster sizes** (~17-20 receptors per cluster instead of ~12) than previously believed.

## Machine Learning Extension

Beyond mechanistic models, I also developed **ML-PWS**, which combines PWS with neural networks to estimate information rates directly from experimental data without requiring detailed mechanistic knowledge. This opens the door to analyzing systems where we don't have complete models.

## Key Contributions

1. First exact Monte Carlo method for computing trajectory mutual information
2. Three efficient computational variants leveraging techniques from statistical physics
3. Extensive studies of the widely-used Gaussian approximation
4. New insights into bacterial receptor organization
5. Machine learning approach for data-driven information quantification

## Access the Thesis

The thesis is freely available online:

- **Interactive web version**: [manuel-rhdt.github.io/webthesis](https://manuel-rhdt.github.io/webthesis/)
- **PDF download**: [ir.amolf.nl/pub/11167](https://ir.amolf.nl/pub/11167)
- **Software implementation**: [PathWeightSampling.jl](https://github.com/manuel-rhdt/PathWeightSampling.jl) (Julia package)

## What's Next

The PWS framework has applications across many fields:
- Neural coding and brain information processing
- Gene regulatory networks and cell signaling
- Design of synthetic biological circuits
- Immunology and receptor signaling
- Population dynamics in ecology

The methods developed in this thesis provide a new toolbox for quantitatively analyzing information transmission in any stochastic system.

---

**Citation:**
Reinhardt, M.J. (2025). *Quantifying the Flow of Information.* PhD Thesis, Vrije Universiteit Amsterdam. [https://doi.org/10.5463/thesis.1092](https://doi.org/10.5463/thesis.1092)

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
