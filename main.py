
# PROGRAM LOGIC
# 2.       Our workbook: This contains our analysis on the weights data.
# A.      Lanes : This sheet has all the data with lanes, origin and Destination and the weights, amount and CPK asscizted with the lanes.
# B.      City_code: This has the data for the City_code(x) function.
# C.      Route_name : this has the data to be returned when route_name(x) function is called.
# D.      Hub_connected_hub: this has the data which HUB_CONNECTED_HUB[] would be having.
# E.      City_Array: This sheet has the data w.r.t the city_array[].

# Now about the Our_Workbook algorithm:

# Input_origin: Input field for Origin from webpage.
# Input_destiantion: Input for Destination from webpage.
# Hub(x) : function that returns the 3 letter Hub name for a 3-letter input x.
# City_code(x): function that returns the 3 letter city_code for a 3-letter input x.
# route() : Binary function that tells us whether a location falls under any route or not.
# get_route_name(x): function that searches the route in which ‘x’ city is mapped and returns an array of all cities in that route.


def get_city_code(city_name):
    """ take city name and return city code"""
    city_code = ''
    return city_code


def get_hub(city_code):
    """ take city code as input and return the hub it belongs to"""
    hub_code = ''
    return hub_code

def get_hub_city_list(hub_code):
    """ take a hub code as input and return back list of cities mapped to the
    hub"""
    city_list = "All cities mapped to the hub"
    return city_list


def has_route(city_code):
    """ take a city code as input and return True if a route exist for that
    city else return False"""
    return True


def get_route_name(city_code):
    """ take city code as input and return the route name it belongs to"""
    route_name = ''
    return route_name


def get_route_cities(route_name):
    """ take route name as input and return all cities under that route"""
    return []


def get_connected_hubs(hub_code):
    """ All hubs connected to the hub. Read this from 'HUB_CONNECTED_HUB sheet"""
    return []


def get_hub_difference(origin_hub, dest_hub):
    """ take two hub code as inputs and return set difference of connected hubs
    of those hubs."""
    return set(get_connected_hubs(dest_hub)) -
           set(get_connected_hubs(origin_hub))


def calculate_cpk(amount, weight):
    return float(amount) / float(weight)

def main(input_origin, input_destination):
    # get city codes
    origin_code = get_city_code(input_origin)
    dest_code = get_city_code(input_destination)
    # get origin and dest hub
    origin_hub = get_hub(input_origin)
    dest_hub = get_hub(input_destination)
    # has origin and destination has route ?
    origin_has_route = has_route(input_origin)
    dest_has_route = has_route(input_destination)
    # get route names
    origin_route_name = get_route_name(input_origin)
    dest_route_name = get_route_name(input_destination)

    # 'array of all cities that come under get_route_name(input_origin)'
    origin_route_city_list = get_route_cities(origin_route_name)
    # 'array of all cities that come under get_route_name(input_destination)'
    dest_route_city_list = get_route_cities(dest_route_name)

    # set difference of connected hubs of origin and destination hubs
    destination_hub_connected_hub_array = get_hub_difference(origin_hub,
                                                             dest_hub)
    # all cities related to destination hub
    dest_hub_city_list = get_hub_city_list(dest_hub)
    # all cities related to origin hub
    origin_hub_city_list = get_hub_city_list(origin_hub)

    if not (origin_code not in origin_hub_city_list and dest_code not in
            dest_hub_city_list and origin_hub == dest_hub):
        return 0

    # CONDITION 1
    if origin_has_route and dest_has_route:
        if origin_route_name != dest_route_name:
            # WHAT DEOS THIS MEANS ? IS IT LIKE ORIGIN PART OF ORIGIN
            # CITY ROUTE LIST ?
            if origin_code in origin_route_city_list and dest_code in dest_route_city_list:
                CPK = calculate_cpk(sum(amount), sum(weight)):
            else
                if origin_code in origin_route_city_list and dest_code in dest_route_city_list:
                    CPK = calculate_cpk(sum(amount), sum(weight)):
                # HERE IT CONTRADICT, SINCE THE ENTIRE BLOCK RUN WITH
                # THE ASSUMPTION THAT ORIGIN AND DESTINATION HAS ROUTE
                # : REFER THIRD IF CONDITION, LINE NUMBER 75
                else origin_has_route and not dest_has_route:
                    # 'array of all cities that come under get_route_name(input_origin)'
                    if origin_code = origin_route_city_list and dest_code = input_destination:
                        CPK = calculate_cpk(sum(amount), sum(weight)):
            elif dest_has_route and not origin_has_route:
                if origin_code = origin_route_city_list and dest_code = dest_route_city_list:
                    CPK = calculate_cpk(sum(amount), sum(weight)):
        elif origin_code in origin_hub_city_list and dest_code in dest_hub_city_list:
            CPK = calculate_cpk(sum(amount), sum(weight)):
    # CONDITION 2
    elif origin_code in origin_hub_city_list and dest_code not in dest_hub_city_list:
        if origin_code in origin_hub_city_list and dest_code == input_destination:
            CPK = calculate_cpk(sum(amount), sum(weight)):
    # CONDITION 3
    elif origin_code  not in origin_hub_city_list and dest_code in dest_hub_city_list:
        if origin_code == input_origin and dest_code in dest_hub_city_list:
            CPK = calculate_cpk(sum(amount), sum(weight)):
    # CONDITION 4
    else
        if origin_code in origin_hub_city_list and dest_code in dest_hub_city_list:
            CPK = calculate_cpk(sum(amount), sum(weight)):
    return CPK
