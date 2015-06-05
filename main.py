

def make_od_pair_excel(od_pair_list):
    # for every O-D pair there will be a row in 'Lanes' Sheet.
    # take those rows and add that into a new excel sheet.
    return 'output.xlsx'

def cross_join(origin_route_city_list, dest_route_city_list):
    """ Cross join two list of cities """
    return [(org, dest) for org in origin_route_city_list
            for dest in dest_route_city_list]

def get_city_code(city_name):
    """ take city name as input and return city code"""
    city_code = ''
    return city_code


def get_hub(city_code):
    """ take city code as input and return the hub it belongs to"""
    hub_code = ''
    return hub_code


def get_connected_hubs(hub_code):
    """ All hubs connected to the hub. Read this from 'HUB_CONNECTED_HUB sheet"""
    hub_list = []
    return hub_list


def get_hub_city_list(hub_code):
    """ take a hub code as input and return back list of cities mapped to the
    hub. This should be read from 'CITY_ARRAY' sheet."""
    city_list = "All cities mapped to the hub"
    return city_list


def get_connected_hub_cities(hub):
    connected_hubs = get_connected_hubs(hub)
    city_list = map(get_hub_city_list, connected_hubs)
    return [item for row in city_list for item in row]


def get_hub_cities_cross_join(origin_hubs, dest_hubs):
    """ take list of origin hubs, and list of destination hubs as input.
    find out the cities related to each hubs. return cross product of origin
    hub related cities and destination hub related cities."""
    origin_cities = map(get_hub_city_list, origin_hubs)
    dest_cities = map(get_hub_city_list, dest_hubs)
    return cross_join(origin_cities, dest_cities)


def has_city_hub(city_code):
    """ take a city code as input and return True if a hub exist in that
    city else return False. This will be read from 'CITY_CODE' sheet."""
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

    # has origin and destination has hub in same city?
    origin_has_hub = has_city_hub(origin_code)
    dest_has_hub = has_city_hub(dest_code)

    # get origin and dest hub
    origin_hub = get_hub(origin_code)
    dest_hub = get_hub(dest_code)

    origin_hub_list = get_connected_hubs(origin_hub)
    dest_hub_list = get_connected_hubs(dest_hub)

    # get route names
    origin_route_name = get_route_name(origin_code)
    dest_route_name = get_route_name(dest_code)

    # 'array of all cities that come under get_route_name(origin_code)'
    origin_route_city_list = get_route_cities(origin_route_name)
    # 'array of all cities that come under get_route_name(dest_code)'
    dest_route_city_list = get_route_cities(dest_route_name)

    # 'array of all cities the comes under related hubs of origin hub
    origin_hubs_city_list = get_connected_hub_cities(origin_hub)
    # 'array of all cities the comes under related hubs of destination hub
    dest_hubs_city_list = get_connected_hub_cities(dest_hub)

    # condition 1: both origin city and dest city does not part of
    # hub city list (CITY_CODE sheet)
    if not origin_has_hub and not dest_has_hub:
        # if and destination are connected to same hub:
        if origin_hub == dest_hub:
            #if both route names are different:
            # take the cartition product of origin city list and
            # destination list.
            if origin_route_name != dest_route_name:
                od_pair_list = cross_join(origin_route_city_list,
                                          dest_route_city_list)
            # origin and destination routes are same:
            # take the cartition product of origin city list.
            else:
                od_pair_list = cross_join(origin_route_city_list,
                                           origin_route_city_list)


        else: # not part of same hub
            # 1. get all cities of origin route - origin_route_city_list
            # 2. get all cities of destination route - dest_route_city_list
            # 3. find cartition cross product of origin_route_cities * dest_route_cities - 1 st lane list
            first_lane_list = cross_join(origin_route_city_list,
                                         dest_route_city_list)
            # 4. get all hubs related to origin hub. - A - excluding origin hub
            # - origin_hub_list
            # 5. get all hubs related to destination hub. - B - dest_hub_list
            # 6. all cities of (A - B) * all cities of (B - A) - 2 nd lane list
            temp_origin_hub_list = get_connected_hubs(origin_hub)
            temp_origin_hub_list.remove(origin_hub)

            origin_hubs = list(set(temp_origin_hub_list) - set(dest_hub_list))
            dest_hubs = list(set(dest_hub_list) - set(origin_hub_list))

            second_lane_list = get_hub_cities_cross_join(origin_hubs, dest_hubs)
            # 7. append 5 and 6 and get sum of weights of all these lanes from 'Lanes' sheet
            od_pair_list = first_lane_list + second_lane_list

    # condition 2: origin part of CITY_CODE sheet and destination city not
    elif origin_has_hub and not dest_has_hub:
        temp_dest_city_list = dest_hubs_city_list + dest_route_city_list
        od_pair_list = cross_join(origin_hubs_city_list, temp_dest_city_list)

    elif not origin_has_hub and dest_has_hub:
        temp_origin_city_list = origin_hubs_city_list + origin_route_city_list
        od_pair_list = cross_join(temp_origin_city_list, dest_hubs_city_list)

    else: # both origin and destination has hub
        od_pair_list = cross_join(origin_hubs_city_list, dest_hubs_city_list)

    file_name = make_od_pair_excel(od_pair_list)
    print file_name
    return file_name
