from check_gnocchi_service import *

def RHELOSP_20236_test():
    out = 1

    out = check_openstack_trait_list()
    if out[0] != 0:
        print("Ceilometer trait list is not found!")
        return 1

    return 0

if __name__ == "__main__":
    res = RHELOSP_20236_test()
    if res == 0:
        print("RHELOSP_20236 Finished successfully")
    else:
        print("RHELOSP_20236 failed")
    sys.exit(res)


