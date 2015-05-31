
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


def main(input_origin, input_destination):
    # get city codes
    origin_code = get_city_code(input_origin)
    dest_code = get_city_code(input_destination)
    # get hub city list
    hub_city_list = get_hub_city_list()
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

    if origin_code not in hub_city_list and dest_code not in hub_city_list:
        if origin_hub = dest_hub:
            if origin_has_route and dest_has_route:
                if origin_route_name != dest_route_name:
                    # WHAT DEOS THIS MEANS ? IS IT LIKE ORIGIN PART OF ORIGIN
                    # CITY ROUTE LIST ?
                    if origin = origin_route_city_list and destination = dest_route_city_list:
                        total_weight=sum(weights);
                        Total_amount=Sum(amount);
                        CPK = (total_amount/total_weight);
                    else
                        # 'array of all cities that come under get_route_name(input_origin)'
                        if(origin = origin_route_city_list and destination = city_array[])
                            total_weight=sum(weights);
                            Total_amount=Sum(amount);
                            CPK = (total_amount/total_weight);
                        # HERE IT CONTRADICT, SINCE THE ENTIRE BLOCK RUN WITH
                        # THE ASSUMPTION THAT ORIGIN AND DESTINATION HAS ROUTE
                        # : REFER LINE NUMBER 75
                        else origin_has_route and not dest_has_route:
                            # 'array of all cities that come under get_route_name(input_origin)'
                            origin_route_city_list = []
                            If(origin = origin_route_city_list and destination = input_destination):
                                total_weight=sum(weights);
                                Total_amount=Sum(amount);
                                CPK = (total_amount/total_weight);
                    elif(has_route(input_origin)=0 and has_route(input_destination)=1)
                        # 'array of all cities that come under get_route_name(input_origin)'
                        dest_route_city_list[] = []
                        if(origin = input_origin and destination = dest_route_city_list[] ):
                            total_weight=sum(weights);
                            Total_amount=Sum(amount);
                            CPK = (total_amount/total_weight);
                else
                    #{All hubs connected to the hub(input_destination)} - {All hubs connected to the hub(input_origin)};
                    #/* Mutually exclusive concept (A-B)*/
                    Destination_hub_connected_hub_array[] = []
                    #Basically make an array of all cities that are connected to the hubs in Destination_hub_connected_hub_array[];
                    Destination_Hub_to_city_array[] = []
                    #{All hubs connected to the hub(input_origin)} - {All hubs connected to the hub(input_destination)};
                    #/* Mutually exclusive concept (B-A) */
                    Origin_hub_connected_hub_array[] = []
                    # Basically make an array of all cities that are connected to the hubs in Origin_hub_connected_hub_array[];
                    Origin_Hub_to_city_array[] = []
                    if(origin = Origin_Hub_to_city_array[] and destination = Destination_Hub_to_city_array[])
                        total_weight=sum(weights);
                        Total_amount=Sum(amount);
                        CPK = (total_amount/total_weight);
            elif(get_city_code(input_origin) is in get_hub_city_list[] and get_city_code(input_destination) is not in get_hub_city_list[]):
                # {All hubs connected to the hub(input_origin)} - {All hubs connected to the hub(input_destination)};
                # /* Mutually exclusive concept (A-B) */
                Origin_hub_connected_hub_array[] = []
                # Basically make an array of all cities that are connected to the hubs in Origin_hub_connected_hub_array[];
                Origin_Hub_to_city_array[] = []
                if(origin = origin_Hub_to_city_array[] and destination = input_destination)
                    total_weight=sum(weights);
                    Total_amount=Sum(amount);
                    CPK = (total_amount/total_weight);
            elif(get_city_code(input_origin) is not in get_hub_city_list[] and get_city_code(input_destination) is in get_hub_city_list[]):
                # {All hubs connected to the hub(input_destination)} - {All hubs connected to the hub(input_origin)};
                # /* Mutually exclusive concept (B-A) */
                Destination_hub_connected_hub_array[] = []
                # Basically make an array of all cities that are connected to the hubs in Destination_hub_connected_hub_array[];
                Destination_Hub_to_city_array[] = []
                if(origin = input_origin and destination = Destination_Hub_to_city_array[]):
                    total_weight=sum(weights);
                    Total_amount=Sum(amount);
                    CPK = (total_amount/total_weight);
            else
                # {All hubs connected to the hub(input_destination)} - {All hubs connected to the hub(input_origin)};
                # /* Mutually exclusive concept (A-B) */
                Destination_hub_connected_hub_array[] = []
                # Basically make an array of all cities that are connected to the hubs in Destination_hub_connected_hub_array[];
                Destination_Hub_to_city_array[] = []
                # {All hubs connected to the hub(input_origin)} - {All hubs connected to the hub(input_destination)};
                # /* Mutually exclusive concept (B-A) */
                Origin_hub_connected_hub_array[] = []
                # Basically make an array of all cities that are connected to the hubs in Origin_hub_connected_hub_array[];
                Origin_Hub_to_city_array[] = []
                if(origin = Origin_Hub_to_city_array[] and destination = Destination_Hub_to_city_array[]):
                    total_weight=sum(weights);
                    Total_amount=Sum(amount);
                    CPK = (total_amount/total_weight);
