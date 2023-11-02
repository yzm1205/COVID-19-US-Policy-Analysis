# [Data-Driven Estimation of Effectiveness of COVID-19 Non-pharmaceutical Intervention Policies](https://ieeexplore.ieee.org/abstract/document/10020822)

## Abstract 
Abstract—Non-pharmaceutical Interventions (NPIs), such as
Stay-at-Home, and Face-Mask-Mandate, are essential components of the public health response to contain an outbreak
like COVID-19. However, it is very challenging to quantify the
individual or joint effectiveness of NPIs and their impact on
people from different racial and ethnic groups or communities
in general. Therefore, in this paper, we study the following two
research questions: 1) How can we quantitatively estimate the
effectiveness of different NPI policies pertaining to the COVID-19
pandemic?; and 2) Do these policies have considerably different
effects on communities from different races and ethnicity? To
answer these questions, we model the impact of an NPI as a
joint function of stringency and effectiveness over a duration of
time. Consequently, we propose a novel stringency function that
can provide an estimate of how strictly an NPI was implemented
on a particular day. Next, we applied two popular tree-based
discriminative classifiers, considering the change in daily COVID
cases and death counts as binary target variables, while using
stringency values of different policies as independent features.
Finally, we interpreted the learned feature weights as the effectiveness of COVID-19 NPIs. Our experimental results suggest that,
at the country level, restaurant closures and stay-at-home policies
were most effective in restricting the COVID-19 confirmed cases
and death cases respectively; and overall, restaurant closing was
most effective in hold-down of COVID-19 cases at individual
community levels such as Asian, White, Black, AIAN and, NHPI.
Additionally, we also performed a comparative analysis between
race-specific effectiveness and country-level effectiveness to see
whether different communities were impacted differently. Our
findings suggest that the different policies impacted communities
(race and ethnicity) differently.

## Computing Impact using Proposed Method
![drawing](https://github.com/yzm1205/COVID-19-US-Policy-Analysis/blob/main/Proposed-Algo.jpg)

## Impact of NPIs on different States of USA
![drawing](https://github.com/yzm1205/COVID-19-US-Policy-Analysis/blob/main/impact-state-wise.png)

## Impact of Different NPIs on Races
![drawing](https://github.com/yzm1205/COVID-19-US-Policy-Analysis/blob/main/race_policy_impact_optimized_v3.png)  
where P's are policies such as **Stay-At-Home, Restaurant Closure, Business-Closure, Face Masks** and **Travel Ban** respectively. 

