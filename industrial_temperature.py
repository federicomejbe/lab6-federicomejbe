def trigger_alarm(temperatures, threshold=80):
    result = []
    for sensor in temperatures:
        if temperatures[sensor] > threshold:
            result.append(sensor)
    return result