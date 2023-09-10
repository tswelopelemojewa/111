import pickle
import sys
import sklearn


with open('models/ababoost_Jn.pkl','rb') as f:
        Jn_model = pickle.load(f)
        pred = Jn_model.predict([[sys.argv[1]]])
        print(pred)
