import simutils as su
import h5py
import os

data_file = "C:\\Users\\mcastle\\Documents\\Web2py\\applications\\bootcamp_1\\private\\data\\dataset_1\\Video_Games_Sales_as_at_22_Dec_2016.csv"
h5_file = "C:\\Users\\mcastle\\Documents\\Web2py\\applications\\bootcamp_1\\private\\data\\data.h5"

df = su.read_csv(data_file)

if os.path.exists(h5_file):
    os.remove(h5_file)

with h5py.File(h5_file, 'w') as f:
    for c in df.columns:
        if df[c].dtype == object:
            col_dt = "S50"
            df[c] = df[c].fillna('')
            new_data = df[c].values.astype(str)
        else:
            col_dt = df[c].dtype
            new_data = df[c].values
        dataset = f.create_dataset('/data/{}'.format(c), df[c].shape, maxshape=df[c].shape, dtype=col_dt)
        dataset[:] = new_data
