# gale_shapley
Python implementation of Gale Shapley (stable marriage) algorithm.

A sample list file is included. It is a simple text file listing hypothetical rankings one 
group of people associates with anotherr (to keep it simple, we'll say it's a list of boys' preferences for girls,
and girls' preferences for boys).

The first 10 lines represent each boy's list of favored girls, in order from most liked to least liked.
The last 10 lines are the same, but for each of the girl's preferences.

As it is coded the stable marriages produced are "boy optimal", that is to say that the resulting marriages maximize
the group "satisfaction" of the boys, while largely ignoring that of the girls. Switching the first 10 lines with the
last 10 would reverse the effect; though the code output will remain the same the user will need to manually swap the 
genders in the associated printouts to achieve a full switch that doesn't require a bit of imagination.
