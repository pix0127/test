# -*- coding: utf-8 -*-
#!/usr/bin/env python

import folium
import pandas as pd

def opendata():
    xl_file = pd.read_csv("data.csv")
    #dfs = {sheet_name: xl_file.parse(sheet_name) for sheet_name in xl_file.sheet_names}
    #print xl_file['location']
def main():
    markers=[]
    location = pd.read_csv("C:\map\cgi-bin\data.csv")
    for a in location['location']:
        temp=a.split(',')
        lat=temp[0].split('(')[1]
        lon=temp[1].split(')')[0]
        if lat!=' NA ' and lon!=' NA ':
            markers.append((float(lat),float(lon)))
    print markers
    

    map_osm = folium.Map(location=[22.6239936,120.5929984],zoom_start=18)
    
    for marker in markers:
        map_osm.simple_marker([marker[0], marker[1]], popup=str(marker))
    map_osm.create_map(path='test.html')
    print "Content-Type: text/html"
    print
    file = open("test.html")
    print file.read()
    file.close()


if __name__=="__main__":
    main()
    opendata()