condition 1: both origin city and dest city does not part of hub city list (CITY_CODE sheet)
--------------------------------------------------------------------------------------------

    if origin and destination are connected to same hub:
        if both route names are different:
            origin_city_list = all cities coming under origin city route
            dest_city_list = all cities coming under dest city route

            take the cartition product of origin city list and destination
            list. for every O-D pair there will be a row in 'Lanes' Sheet.
            Take the sum of weight
        else origin and destination routes are same:
            take the cartition product of origin city list.
            for every O-D pair there will be a row in 'Lanes' Sheet.
            Take the sum of weight.

    else: not part of same hub
        1. get all cities of origin route (origin_route_cities)
        2. get all hubs related to origin hub. (origin_related_hub_list) - A - not including origin hub
        3. get all cities of destination route (dest_route_cities)
        4. get all hubs related to destination hub. (dest_related_hub_list) - B
        5. find cartition cross product of origin_route_cities * dest_route_cities - 1 st lane list
        6. all cities of (A - B) * all cities of (B - A) - 2 nd lane list
        7. append 5 and 6 and get sum of weights of all these lanes from 'Lanes' sheet

condition 2: origin part of CITY_CODE sheet and destination city not
-------------------------------------------------------------------
    1. get origin hub - OH
    2. get all the connected hubs from HUB_CONNECTED_HUB sheet - OHL
    3. cities of all these hubs - OCL = cities(OH + OHL)
    4. get destination hub - DH
    5. get all the hubs connected to DH. - DHL
    6. get all cities of DHL - DHCL = cities(DHL)
    7. get destination city route - DR
    8. get all cities of DRCL (Destination Route City List)
    9. destination cities will be - DCL = DHCL + DRCL
    10. take cartition cross product of  OCL * DCL and get sum of weights of all these lanes from 'Lanes' sheet


condition 3: destination part of CITY_CODE sheet and origin city not
-------------------------------------------------------------------
    - reverse of the above codition


condition 4: both origin city and dest city are part of hub city list (CITY_CODE sheet)
---------------------------------------------------------------------------------------
    1. get origin hub - OH
    2. get all the connected hubs from HUB_CONNECTED_HUB sheet - OHL
    3. cities of all these hubs - OCL = cities(OH + OHL)
    4. get destination hub - DH
    5. get all the connected hubs from HUB_CONNECTED_HUB sheet - DHL
    6. cities of all these hubs - DCL = cities(DH + DHL)
    7. take cartition cross product of  OCL * DCL and get sum of weights of all these lanes from 'Lanes' sheet


data structures used
--------------------
    city_hub_mapping = {'AHD': {'hub':'AHH', 'route':'AHD'}, .....}

    hub_connected_hub_mapping = {'VTZ': ['DEH', 'HNH', 'HYH']}

    hub_city_list_mapping = {'SXR': [ 'GND', 'SOO', 'ANA', 'KUL', 'BUD', 'BAA', 'SYN'], ..}

    city_has_hub_mapping = {'CJH': 'CJT', ..} # city_code sheet

    routename_cities_mapping = {'AHD': ['AHD',.],  ...}
