# Decentralized power distribution
Proof of concept to draw power efficiently in a decentralized manner from a restricted source.

The original idea was developed to make large electricity consumer devices access a grid assuming that there is a larger consumer capacity then what the grid may be able to serve.

Yet the very same approach can likely also be used or abused to influence market pricing in an environment, where the power producer(s) may form an oligopol or monopol market.

## The concept

Randomly switch consumers on and off to maintain a balanced load on the system, so that bigger the consumption the higher the chance to switch it off. A hash generated pseudo random number is compared to an integrating regulator value to determine by chance if a device shall draw power from the grid. The higher a device's consumption the lower its chance of being connected. All this ultimately results in a fairly balanced power being drawn from the grid.
