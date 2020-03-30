# AI20S - HW0
# Student ID                : R08922a02
# English Name              : Shuo-En
# Chinese Name (optional)   : 張碩恩


# Import packages here
import sklearn
from sklearn.linear_model import LinearRegression
import numpy as np


class Predictor:
    def __init__(self, dataset_path='salary_data.csv'):
        self.test = 0
        self.dataset_data, self.dataset_target = self.read_csv(dataset_path)
        self.model = self.train()

    @staticmethod
    def read_csv(file_path='salary_data.csv'):
        # Implement your CSV file reading here
        # returns data, target
        # Both outputs should be in numpy array format with type np.float64
        # You may reshape the array if necessary
        # raise NotImplementedError
        salary_data = np.genfromtxt(file_path, delimiter=',')
        salary_data = salary_data[1:]
        data = np.float64(salary_data[:,0])
        data = data.reshape(-1, 1)
        target = np.float64(salary_data[:,1])
        return data, target

    def train(self):
        # returns sklearn's fitted LinearRegression model
        # Remember to pass self.dataset_data and self.dataset_target as its parameters
        # raise NotImplementedError
        reg = LinearRegression().fit(self.dataset_data, self.dataset_target)
        return reg


    def predict(self, x):
        # returns model's prediction given x as input
        # raise NotImplementedError
        y = self.model.predict(x)
        return y

    def write_prediction(self, x, write_path='prediction.txt'):
        # opens a file using write_path with a writeable access
        # write all the outputs from the model's prediction to the file
        # You must write the output line by line instead of writing its numpy array or list object
        # This method does not return anything
        # raise NotImplementedError
        y = self.predict(x)
        with open(write_path, 'w') as predict:
            for i in range(len(y)):
                predict.write("{:0.2f}".format(y[i]) + '\n')


if __name__ == '__main__':
    # You may test your program here
    # Anything residing in this block will not be graded
    pred = Predictor()
    dataset_data, dataset_target = pred.read_csv()
    pred.write_prediction(dataset_data)