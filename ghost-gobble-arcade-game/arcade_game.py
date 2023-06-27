eat_ghost = lambda power_pellet_active, touching_ghost: power_pellet_active and touching_ghost

score = lambda touching_power_pellet, touching_dot: touching_power_pellet or touching_dot

lose = lambda power_pellet_active, touching_ghost: not power_pellet_active and touching_ghost

win = lambda has_eaten_all_dots, power_pellet_active, touching_ghost: has_eaten_all_dots and not lose(
    power_pellet_active, touching_ghost)
