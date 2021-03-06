from check_gnocchi_service import *

def RHELOSP_34680_test():
    res = 1

    #0. Operate under admin user
    res = switch_context(orig_rc)
    if res != 0:
        return 1

    #1. Get resource_id of admin user
    res, admin_id = get_resource_id("user", "admin")
    if res != 1:
        res = 0
    else:
        return 1


    #2. Switch to demo user
    res = switch_context(demo_rc)
    if res != 0:
        return 1

    #3. Under demo user check that there are no admin resources
    res = find_metrics(admin_id, "image")
    if res[0] != 0:
        return 1
    else:
        if res[1] == "Found":
            print "Found admin metrics under demo!"
            return 1
        elif res[1]=="Not found":
            print "Did not find admin metrics under demo!"
            res = 0

    return 0

    #4. Get back under admin
    res = switch_context(orig_rc)
    if res != 0:
        return 1

    #5. Under admin get a metric id of a resource
    res = test_new_resource("image", resource_id)
    if res != 0:
        return 1

    #6. Check the measures of the resource
    res = test_values_assigned(resource_id, image_value_check[0])
    if not 'Forbidden' in res[1]:
       return 1
    else:
        res = 0


if __name__ == "__main__":
    res = RHELOSP_34680_test()
    if res == 0:
        print("RHELOSP_34680_test Finished successfully")
    else:
        print("RHELOSP_34680_test failed")
    sys.exit(res)