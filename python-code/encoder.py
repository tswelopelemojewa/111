from sklearn.preprocessing import LabelEncoder
import pandas as pd

data1 = pd.read_excel("public\dataset\complete_data.xlsx")

data = pd.read_excel("public\dataset\complete_data.xlsx")

data = data.dropna()

# loop through the columns in the dataframe where type is "object"
for col in data.select_dtypes(include=["object"]).columns:
    # initialize a label encoder
    label_encoder = LabelEncoder()

    # fit the encoder to the unique values in the columns
    label_encoder.fit(data[col])

    # transform the column usinf the encode
    data[col] = label_encoder.transform(data[col])

    # print the columns names and the unique encoded values
    # print(f"{col}: {dat/a[col]}")

# print(data.columns)

columns_to_drop_Jn = ['Borehole ID', 'Depth From (m)', 'Depth to (m)', 'Run Length (m)',
                      'True Thickness (m)', 'Weathering', 'Hardness', 'Geotech Domain',
                      'Jr Description', 'Ja Description', 'Jw Description',
                      'ESR Conditions', 'Depth underground (m)', 'RQD m', 'RQD %', 'Jn', 'Jr',
                      'Ja', 'Jw', 'Density', 'Virgin Stress', 'UCS Mpa',
                      'UCS/Virgin stress ratio', 'SRF', 'Q Value', 'LNQ', 'RMR', 'ESR VALUE',
                      'Maximum unsupported span']

columns_to_drop_Ja = ['Borehole ID', 'Depth From (m)', 'Depth to (m)', 'Run Length (m)',
                      'True Thickness (m)', 'Weathering', 'Hardness', 'Geotech Domain',
                      'Jn Description', 'Jr Description', 'Jw Description',
                      'ESR Conditions', 'Depth underground (m)', 'RQD m', 'RQD %', 'Jn', 'Jr',
                      'Ja', 'Jw', 'Density', 'Virgin Stress', 'UCS Mpa',
                      'UCS/Virgin stress ratio', 'SRF', 'Q Value', 'LNQ', 'RMR', 'ESR VALUE',
                      'Maximum unsupported span']
columns_to_drop_Jr = ['Borehole ID', 'Depth From (m)', 'Depth to (m)', 'Run Length (m)',
                      'True Thickness (m)', 'Weathering', 'Hardness', 'Geotech Domain',
                      'Jn Description', 'Ja Description', 'Jw Description',
                      'ESR Conditions', 'Depth underground (m)', 'RQD m', 'RQD %', 'Jn', 'Jr',
                      'Ja', 'Jw', 'Density', 'Virgin Stress', 'UCS Mpa',
                      'UCS/Virgin stress ratio', 'SRF', 'Q Value', 'LNQ', 'RMR', 'ESR VALUE',
                      'Maximum unsupported span']
columns_to_drop_Jw = ['Borehole ID', 'Depth From (m)', 'Depth to (m)', 'Run Length (m)',
                      'True Thickness (m)', 'Weathering', 'Hardness', 'Geotech Domain',
                      'Jn Description', 'Jr Description', 'Ja Description',
                      'ESR Conditions', 'Depth underground (m)', 'RQD m', 'RQD %', 'Jn', 'Jr',
                      'Ja', 'Jw', 'Density', 'Virgin Stress', 'UCS Mpa',
                      'UCS/Virgin stress ratio', 'SRF', 'Q Value', 'LNQ', 'RMR', 'ESR VALUE',
                      'Maximum unsupported span']
columns_to_drop_esr = ['Borehole ID', 'Depth From (m)', 'Depth to (m)', 'Run Length (m)',
                       'True Thickness (m)', 'Weathering', 'Hardness', 'Geotech Domain',
                       'Jn Description', 'Jr Description', 'Ja Description', 'Jw Description',
                       'Depth underground (m)', 'RQD m', 'RQD %', 'Jn', 'Jr',
                       'Ja', 'Jw', 'Density', 'Virgin Stress', 'UCS Mpa',
                       'UCS/Virgin stress ratio', 'SRF', 'Q Value', 'LNQ', 'RMR', 'ESR VALUE',
                       'Maximum unsupported span']

# Encoded values
df_Jn = data.drop(columns_to_drop_Jn, axis=1)
df_Jr = data.drop(columns_to_drop_Jr, axis=1)
df_Ja = data.drop(columns_to_drop_Ja, axis=1)
df_Jw = data.drop(columns_to_drop_Jw, axis=1)
df_esr = data.drop(columns_to_drop_esr, axis=1)

# Non encoded values 
df1_Jn = data1.drop(columns_to_drop_Jn, axis=1)
df1_Jr = data1.drop(columns_to_drop_Jr, axis=1)
df1_Ja = data1.drop(columns_to_drop_Ja, axis=1)
df1_Jw = data1.drop(columns_to_drop_Jw, axis=1)
df1_esr = data1.drop(columns_to_drop_esr, axis=1)


# # Printing out the encoded values 

# with open("public/Jn.txt", "w") as output:
#     for var in values_Jn:
#         output.write(str(var) + '\n')
# values_Jr = df_Jr
# with open("public/Jr.txt", "w") as output:
#     for var in values_Jr["Jr Description"]:
#         output.write(str(var) + '\n')
# values_Ja = df_Ja
# with open("public/Ja.txt", "w") as output:
#     for var in values_Ja["Ja Description"]:
#         output.write(str(var) + '\n')
# values_Jw = df_Jw
# with open("public/Jw.txt", "w") as output:
#     for var in values_Jw["Jw Description"]:
#         output.write(str(var) + '\n')
# values_esr = df_esr
# with open("public/esr.txt", "w") as output:
#     for var in values_esr["ESR Conditions"]:
#         output.write(str(var) + '\n')

# # Printing out the non encoded values 
# values_nesr = df1_esr
# with open("public/esrnon.txt", "w") as output:
#     for var in values_nesr["ESR Conditions"]:
#         output.write(str(var) + '\n')
values_Jn = list(df_Jn["Jn Description"])
values_Jnnon = list(df1_Jn["Jn Description"])
with open("public/Jnnon.txt", "w") as output:
    for i in range(0, len(values_Jn) - 1):
        output.write('"'+ str(values_Jnnon[i] + '(' + str(values_Jn[i])) + ")" +'"' +','+ '\n')

# values_Jntext = df1_esr
# with open("public/JnText.txt", "w") as output:
#     for var in values_Jntext["Jn Description"]:
#         output.write(str(var) + '\n')

# Jr Values 
values_Jr = list(df_Jr["Jr Description"])
values_Jrnon = list(df1_Jr["Jr Description"])
with open("public/Jrnon.txt", "w") as output:
    for i in range(0, len(values_Jr) - 1):
        output.write('"'+ str(values_Jrnon[i] + '(' + str(values_Jr[i])) + ")" +'"' +','+ '\n')

# Ja values
values_Ja = list(df_Ja["Ja Description"])
values_Janon = list(df1_Ja["Ja Description"])
with open("public/Janon.txt", "w") as output:
    for i in range(0, len(values_Ja) - 1):
        output.write('"'+ str(values_Janon[i] + '(' + str(values_Ja[i])) + ")" +'"' +','+ '\n')

# Jw Values 
values_Jw = list(df_Jw["Jw Description"])
values_Jwnon = list(df1_Jw["Jw Description"])
with open("public/Jwnon.txt", "w") as output:
    for i in range(0, len(values_Jw) - 1):
        output.write('"'+ str(values_Jwnon[i] + '(' + str(values_Jw[i])) + ")" +'"' +','+ '\n')


# ESR values 
# Jw Values 
# Jw Values 
values_esr = list(df_esr["ESR Conditions"])
values_esrnon = list(df1_esr["ESR Conditions"])
with open("public/esrnon.txt", "w") as output:
    for i in range(0, len(values_esr) - 1):
        output.write('"'+ str(values_esrnon[i] + '(' + str(values_esr[i])) + ")" +'"' +','+ '\n')

