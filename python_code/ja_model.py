import pickle
import sys


with open('models/gradient_boosting_Ja.pkl','rb') as f:
    Ja_model = pickle.load(f)
    
    print(Ja_model.predict([[sys.argv[1]]]))