# PDDL plan generation

## Generate a plan

Use your favorite planner to generate a plan

In this folder you find some examples of PDDL based plan generation through the [planning.domains](http://planning.domains/)

Let `ER.pddlout` be the output of the planner (i.e., the generated plan).

## Define Execution Rules

Define execution rules in a file `ER.er`

## Generate the PNP

Use the following command to generate a PNP

    pnpgen_linear ER.pddlout ER.er


