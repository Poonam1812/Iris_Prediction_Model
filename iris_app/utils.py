import numpy as np
import pickle
import config

class Iris():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm=SepalLengthCm
        self.SepalWidthCm=SepalWidthCm
        self.PetalLengthCm=PetalLengthCm
        self.PetalWidthCm=PetalWidthCm

    def load_model(self):
        with open(config.model_file_path, 'rb') as f:
            self.model=pickle.load(f)
        
    def get_predicted_species(self):
        self.load_model()
        test_array=np.zeros(4)
        
        test_array[0]=self.SepalLengthCm
        test_array[1]=self.SepalWidthCm
        test_array[2]=self.PetalLengthCm
        test_array[3]=self.PetalWidthCm

        print("test array",test_array)
        
        predicted_species = self.model.predict([test_array])[0]
        return predicted_species


#if __name__ == "__main__":
   # SepalLengthCm =4.5
  #  SepalWidthCm = 3.2
   # PetalLengthCm = 1.1
   # PetalWidthCm = 0.4  

   # pred_spec= Iris(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
  #pred__spec.get_predicted_species()