def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    efficiency = (voltage * current / theoretical_max_power) * 100
    case = {
        efficiency >= 80: 'green',
        80 > efficiency >= 60: 'orange',
        60 > efficiency >= 30: 'red',
        30 > efficiency: 'black'
    }
    return case.get(True)


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    nuke = temperature * neutrons_produced_per_second
    return 'LOW' if nuke < threshold * .9 else 'NORMAL' if threshold * .9 <= nuke <= threshold * 1.1 else 'DANGER'
