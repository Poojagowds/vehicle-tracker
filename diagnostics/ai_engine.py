def predict_failure(engine_temp, oil_pressure, battery_voltage):

    risk = 0
    dtc = "OK"
    message = "Vehicle operating normally"

    if engine_temp > 110:
        risk += 40
        dtc = "P0217"
        message = "Engine overheating risk"

    if oil_pressure < 20:
        risk += 30
        dtc = "P0520"
        message = "Low oil pressure detected"

    if battery_voltage < 11.5:
        risk += 30
        dtc = "P0562"
        message = "Battery voltage low"

    return risk, dtc, message