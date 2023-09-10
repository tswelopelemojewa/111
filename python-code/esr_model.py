import pickle
import sys
import sklearn

with open('models/model_LR_esr.pkl','rb') as f:
    esr_model = pickle.load(f)
    print(esr_model.predict([[sys.argv[1]]]))

