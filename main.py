
# PROGRAM LOGIC
# 2.       Our workbook: This contains our analysis on the weights data.
# A.      Lanes : This sheet has all the data with lanes, origin and Destination and the weights, amount and CPK asscizted with the lanes.
# B.      City_code: This has the data for the City_code(x) function.
# C.      Route_name : this has the data to be returned when route_name(x) function is called.
# D.      Hub_connected_hub: this has the data which HUB_CONNECTED_HUB[] would be having.
# E.       City_Array: This sheet has the data w.r.t the city_array[].

# Now about the Our_Workbook algorithm:

# Input_origin: Input field for Origin from webpage.
# Input_destiantion: Input for Destination from webpage.
# Hub(x) : function that returns the 3 letter Hub name for a 3-letter input x.
# City_code(x): function that returns the 3 letter city_code for a 3-letter input x.
# route() : Binary function that tells us whether a location falls under any route or not.
# route_name(x): function that searches the route in which ‘x’ city is mapped and returns an array of all cities in that route.

def get_city_code(city_name):
    """ take city name and return city code"""
    city_code = ''
    return city_code

def get_hub_city_list(hub_code):
    """ take a hub code as input and return back list of cities mapped to the
    hub"""
    city_list = "All cities mapped to the hub"
    return city_list


def main():
    if get_city_code(input_origin) not in get_hub_city_list() and get_city_code(input_destination) not in get_hub_city_list():
        {
        if(hub(input_origin) = hub(input_destination))
            {
            if( Route(input_origin)=1 || Route(input_destination)=1)
                {
                if(Route(input_origin)=1 && Route(input_destination=1))
                    {
                    if(route_name(input_origin) != route_name(input_destination)
                        {
                        # 'array of all cities that come under route_name(input_origin)'
                        Origin_city_array[] = []
                        # 'array of all cities that come under route_name(input_destination)'
                        Destination_city_array[] = []
                        if(origin = Origin_city_array[] && destination = Destination_city_array[]):
                            {
                            total_weight=sum(weights);
                            Total_amount=Sum(amount);
                            CPK = (total_amount/total_weight);
                            }
                        else
                            {
                            # 'array of all cities that come under route_name(input_origin)'
                            city_array[] = []
                            if(origin = city_array[] && destination = city_array[])
                                {
                                total_weight=sum(weights);
                                Total_amount=Sum(amount);
                                CPK = (total_amount/total_weight);
                                }
                            }
                        else(Route(input_origin)=1 && Route(input_destination)=0)
                            {
                            # 'array of all cities that come under route_name(input_origin)'
                            Origin_city_array[] = []
                            If(origin = Origin_city_array[] && destination = input_destination):
                                {
                                total_weight=sum(weights);
                                Total_amount=Sum(amount);
                                CPK = (total_amount/total_weight);
                                }
                            }
                        elif(Route(input_origin)=0 && Route(input_destination)=1)
                            {
                            # 'array of all cities that come under route_name(input_origin)'
                            Destination_city_array[] = []
                            if(origin = input_origin && destination = Destination_city_array[] ):
                                {
                                total_weight=sum(weights);
                                Total_amount=Sum(amount);
                                CPK = (total_amount/total_weight);
                                }
                            }
                        }
                    else
                        {
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
                        if(origin = Origin_Hub_to_city_array[] && destination = Destination_Hub_to_city_array[])
                            {
                            total_weight=sum(weights);
                            Total_amount=Sum(amount);
                            CPK = (total_amount/total_weight);
                            }
                        }
                    }
                elif(get_city_code(input_origin) is in get_hub_city_list[] && get_city_code(input_destination) is not in get_hub_city_list[]):
                    {
                    # {All hubs connected to the hub(input_origin)} - {All hubs connected to the hub(input_destination)};
                    # /* Mutually exclusive concept (A-B) */
                    Origin_hub_connected_hub_array[] = []
                    # Basically make an array of all cities that are connected to the hubs in Origin_hub_connected_hub_array[];
                    Origin_Hub_to_city_array[] = []
                    if(origin = origin_Hub_to_city_array[] && destination = input_destination)
                        {
                        total_weight=sum(weights);
                        Total_amount=Sum(amount);
                        CPK = (total_amount/total_weight);
                        }
                    }
                elif(get_city_code(input_origin) is not in get_hub_city_list[] && get_city_code(input_destination) is in get_hub_city_list[]):
                    {
                    # {All hubs connected to the hub(input_destination)} - {All hubs connected to the hub(input_origin)};
                    # /* Mutually exclusive concept (B-A) */
                    Destination_hub_connected_hub_array[] = []
                    # Basically make an array of all cities that are connected to the hubs in Destination_hub_connected_hub_array[];
                    Destination_Hub_to_city_array[] = []
                    if(origin = input_origin && destination = Destination_Hub_to_city_array[]):
                        {
                        total_weight=sum(weights);
                        Total_amount=Sum(amount);
                        CPK = (total_amount/total_weight);
                        }
                    }
                else
                    {
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
                    if(origin = Origin_Hub_to_city_array[] && destination = Destination_Hub_to_city_array[]):
                        {
                        total_weight=sum(weights);
                        Total_amount=Sum(amount);
                        CPK = (total_amount/total_weight);
                        }
                    }
                }
            }
        }
