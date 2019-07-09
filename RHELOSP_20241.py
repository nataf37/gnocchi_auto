from check_gnocchi_service import *

def RHELOSP_20241_test():
    out = 1
    alarm1 = "gnocchi_aggregation_by_metrics_threshold"
    threshold1 = 4.0
    metrics1 = "disk.usage"
    #alarm2 = "gnocchi_aggregation_by_metrics_threshold"
    #threshold2 = 5.0
    #metrics2 = "disk.capacity"

    out1 = create_aodh_alarm(alarm1, threshold1, metrics1)
    if out1[0] != 0:
        print("Aodh alarm %s 1 couldn't be created!" % alarm1)
        return 1

    #out2 = create_aodh_alarm(alarm2, threshold2, metrics2)
    #if out2[0] != 0:
    #    print("Aodh alarm %s 2 couldn't be created!" % alarm2)
    #    return 1

    #out = create_aodh_composition_alarm(out1[1], out2[1])
    #if out != 0:
    #   print("Aodh composition alarm couldn't be created!")
    #   return 1

    event_name="alarm.creation"
    out = ceilometer_filter_by_trait(event_name)
    if out[0] != 0:
        print("Event not found in the list!")
        return 1
    return 0

if __name__ == "__main__":
    res = RHELOSP_20241_test()
    if res == 0:
        print("RHELOSP_20241 Finished successfully")
    else:
        print("RHELOSP_20241 failed")
    sys.exit(res)