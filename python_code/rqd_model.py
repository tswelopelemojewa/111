import pickle
import sys

with open('models/rqd_GBR_rqd.pkl','rb') as f:
        RQD_model_GBR = pickle.load(f)
        print(RQD_model_GBR.predict([[sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]]))

