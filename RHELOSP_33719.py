from check_gnocchi_service import *

def RHELOSP_33719_test():
    res = 1, ''

    #Test the docker processes

    processes_list=aodh_process_list+panko_process_list+ceilometer_process_list+gnocchi_process_list
    for pr in processes_list:
        print("Checking that %s processes run" % (pr))

        res = check_podman_process(pr)
        if res == 0:
            print ("The process %s exists!"%pr)
            return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_33719_test()
    if res == 0:
        print("RHELOSP_33719 Finished successfully")
    else:
        print("RHELOSP_33719 failed")
    sys.exit(res)
