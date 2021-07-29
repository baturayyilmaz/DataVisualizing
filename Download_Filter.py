import urllib.request
import csv
import zipfile
import pandas as pd
import shapefile
import pyproj


# Retrieving Trip Record Data (1 iteration of this code is enough for retrieving the csv file)
urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/trip+data/"+ \
                               "yellow_tripdata_2019-01.csv",
                               "nyc.2019-01.csv")




### FILTERING OUT THE DOWNLOADED CSV FILE, AND WRITING IT TO A NEW CSV FILE ###
fin = open('nyc.2019-01.csv', 'r')
fout = open('nyc.2019-01-01.csv', 'w', newline='')  # newline='' is for getting rid of EXTRA newline after each row

reader = csv.reader(fin)
writer = csv.writer(fout)

columnNames = next(reader)  # getting column names from the csv file
writer.writerow(columnNames)  # writing the columns to the new file

for row in reader:
    if row[1].startswith('2019-01-01'):  # filtering out the downloaded csv file. It only takes the rows where pickup datetime is 1st of January in 2019
        writer.writerow(row)

fin.close()
fout.close()




# Download the location Data
urllib.request.urlretrieve("https://s3.amazonaws.com/nyc-tlc/misc/taxi_zones.zip", "taxi_zones.zip")
with zipfile.ZipFile("taxi_zones.zip","r") as zip_ref:
    zip_ref.extractall("./shape")


def get_lat_lon(sf):
    content = []
    for sr in sf.shapeRecords():
        shape = sr.shape
        rec = sr.record
        loc_id = rec[shp_dic['LocationID']]

        x = (shape.bbox[0] + shape.bbox[2]) / 2
        y = (shape.bbox[1] + shape.bbox[3]) / 2

        content.append((loc_id, x, y))
    return pd.DataFrame(content, columns=["LocationID", "longitude", "latitude"])


def HourColumn(row):
    pickup_datetime = pd.to_datetime(row["tpep_pickup_datetime"]).time()
    hour = pickup_datetime.hour
    return hour


df = pd.read_csv("nyc.2019-01-01.csv")
df["Pickup_Hour"] = df.apply(HourColumn, axis=1) # Creating a Pickup_Hour column. It is created for easing our job while plotting graphs.

sf = shapefile.Reader("shape/taxi_zones.shp")
fields_name = [field[0] for field in sf.fields[1:]]
shp_dic = dict(zip(fields_name, list(range(len(fields_name)))))
attributes = sf.records()
shp_attr = [dict(zip(fields_name, attr)) for attr in attributes]
df_loc = pd.DataFrame(shp_attr).join(get_lat_lon(sf).set_index("LocationID"), on="LocationID") # in this dataset, there are X and Y coordinates instead of lat and lon values

wgs84 = pyproj.Proj("+init=EPSG:4326")
UTM = pyproj.Proj("+init=EPSG:2263")  # UTM coords
df_loc['longitude'], df_loc['latitude'] = pyproj.transform(UTM, wgs84, df_loc['longitude'].tolist(), df_loc['latitude'].tolist()) # the above function was creating UTM coordinates, so they should be converted to latitude and longitude values.

df_joined = df.set_index('PULocationID').join(df_loc.set_index('LocationID')) # joining location data by PickupLocation
df_joined = df_joined.sort_values(by=["Pickup_Hour"], ascending=True)


df_joined.to_csv("NYC-LOC.csv") # Writing joined dataset to a csv, so that we can use it in Dash application.






