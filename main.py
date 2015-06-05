import xlrd
from collections import defaultdict
from report_api import ReportGenerator

wb = xlrd.open_workbook('project.xls')

# dictionary holding city to hub and routename mapping
# city_hub_mapping = {'AHD': {'hub':'AHH', 'route':'AHD'}, .....}
city_hub_mapping = defaultdict(dict)

# all cities mapped to particular route
# {'AHD': ['AHD',.],  ...}
routename_cities_mapping = defaultdict(list)

# hub to city mapping
# = {'SXR': [ 'GND', 'SOO', 'ANA', 'KUL', 'BUD', 'BAA', 'SYN'], ..}
hub_city_list_mapping = defaultdict(list)

# list of hubs connected to one hub
# = {'VTZ': ['DEH', 'HNH', 'HYH']}
hub_connected_hub_mapping = defaultdict(list)

# = {'CJH': 'CJT', ..} # city_code sheet
# city_has_hub_mapping

def make_city_hub_mapping():
    """ city_hub_mapping = {'AHD': {'hub':'AHH', 'route':'AHD', 'has_hub': True}, .....}"""
    # creating hub city list mapping
    city_array_sheet = wb.sheet_by_name('CITY_ARRAY')
    cols_count = city_array_sheet.ncols

    for col in range(cols_count):
        hub_city_list = city_array_sheet.col_values(col)
        cleaned_column = [x for x in hub_city_list if x]
        if cleaned_column:
            hub_name = cleaned_column[0]
            hub_city_list_mapping[hub_name] = cleaned_column[1:]

    # creating city - hub - route mapping
    lookup_sheet = wb.sheet_by_name('lookup sheet')
    city_codes = lookup_sheet.col_values(1)[1:]
    route_names = lookup_sheet.col_values(3)[1:]
    hubs = lookup_sheet.col_values(5)[1:]
    data = zip(city_codes, route_names, hubs)

    for city, route, hub in data:
        city_hub_mapping[city]['has_hub'] = False
        city_hub_mapping[city]['hub'] = hub
        city_hub_mapping[city]['route'] = route


    # creating hub connected hub mapping
    hub_connected_hub_sheet = wb.sheet_by_name('HUB_CONNECTED_HUB')
    cols_count = hub_connected_hub_sheet.ncols
    for col in range(cols_count):
        data_list = hub_connected_hub_sheet.col_values(col)
        cleaned_column = [x for x in data_list if x]
        if cleaned_column:
            hub_name = cleaned_column[0]
            cleaned_cities = filter(lambda x: x.strip(), cleaned_column[1:])
            hub_connected_hub_mapping[hub_name] = cleaned_cities

    # updating the city_hub boolean
    city_code_sheet = wb.sheet_by_name('CITY_CODE')
    hubs = city_code_sheet.col_values(0)[1:]
    cities = city_code_sheet.col_values(1)[1:]
    data = zip(hubs, cities)

    for h, c in data:
        city_hub_mapping[c]['has_hub'] = True

    # creating route city list mapping
    route_name_sheet = wb.sheet_by_name('ROUTE_NAME')
    cols_count = route_name_sheet.ncols
    for col in range(cols_count):
        data_list = route_name_sheet.col_values(col)
        cleaned_column = [x for x in data_list if x]
        if cleaned_column:
            route_name = cleaned_column[0]
            routename_cities_mapping[route_name] = cleaned_column[1:]


    return True

def read_lanes_sheet(origin, destination):
    lanes_sheet = wb.sheet_by_name('Lanes')
    return 0


def make_od_pair_excel(od_pair_list):
    # for every O-D pair there will be a row in 'Lanes' Sheet.
    # take those rows and add that into a new excel sheet.
    report = ReportGenerator('output.xlsx')
    report.write_header(('Origin', 'Destination', 'Weight'))

    for origin, destination in od_pair_list:
        weight = read_lanes_sheet(origin, destination)
        report.write_row((origin, destination, weight))

    report.manual_sheet_close()
    return report.file_name


def cross_join(origin_route_city_list, dest_route_city_list):
    """ Cross join two list of cities """
    return [(org, dest) for org in origin_route_city_list
            for dest in dest_route_city_list]


def get_hub(city_code):
    """ take city code as input and return the hub it belongs to"""
    return city_hub_mapping.get(city_code).get('hub')


def get_connected_hubs(hub_code):
    """ All hubs connected to the hub. Read this from 'HUB_CONNECTED_HUB sheet"""
    return hub_connected_hub_mapping.get(hub_code)


def get_hub_city_list(hub_code):
    """ take a hub code as input and return back list of cities mapped to the
    hub. This should be read from 'CITY_ARRAY' sheet."""
    return hub_city_list_mapping.get(hub_code)


def get_connected_hub_cities(hub):
    connected_hubs = get_connected_hubs(hub)
    city_list = map(get_hub_city_list, connected_hubs)
    return [item for row in city_list for item in row if row]


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
    return city_hub_mapping.get(city_code).get('has_hub')


def get_route_name(city_code):
    """ take city code as input and return the route name it belongs to"""
    return city_hub_mapping.get(city_code).get('route')


def get_route_cities(route_name):
    """ take route name as input and return all cities under that route"""
    return routename_cities_mapping.get(route_name)


def main(origin_code, dest_code):
    # has origin and destination has hub in same city?
    origin_has_hub = has_city_hub(origin_code)
    dest_has_hub = has_city_hub(dest_code)

    # get origin and dest hub
    origin_hub = get_hub(origin_code)
    dest_hub = get_hub(dest_code)

    origin_hub_list = get_connected_hubs(origin_hub)
    dest_hub_list = get_connected_hubs(dest_hub)

    # LKH Exception
    if 'LKH' in origin_hub_list:
        for h in dest_hub_list:
            if 'LKH' in get_connected_hubs(h):
                origin_hub_list.remove('LKH')
                break

    # get route names
    origin_route_name = get_route_name(origin_code)
    dest_route_name = get_route_name(dest_code)


    print 'Origin has hub         :', origin_has_hub
    print 'Destination has hub    :', dest_has_hub
    print 'Origin hub             :', origin_hub
    print 'Destination hub        :', dest_hub
    print 'Origin hub list        :', origin_hub_list
    print 'Destination hub list   :', dest_hub_list
    print 'Origin route name      :', origin_route_name
    print 'Destination route name :', dest_route_name


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
    return file_name


if __name__ == '__main__':
    make_city_hub_mapping()
    main('DEL', 'SAL')
