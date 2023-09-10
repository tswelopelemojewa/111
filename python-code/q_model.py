import pickle
import sys


with open('models/q.pkl','rb') as f:
        q_model = pickle.load(f)
        print(q_model.predict([[sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]]))
