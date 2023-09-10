import pickle
import sys

with open('models/rmr.pkl','rb') as f:
        rmr_model = pickle.load(f)
        print(rmr_model.predict([[sys.argv[1]]]))

