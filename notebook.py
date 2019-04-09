import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('posts_clean.csv', low_memory=False)
data = pd.DataFrame(data.sample(frac=1))


##############

training = data[:int(len(data) * 0.85)]
testing = data[len(training):]

x_training = training.drop("Post Score", axis=1)
x_training = x_training.drop("Post Comments", axis=1)
y_training = training["Post Score"]

x_testing = testing.drop("Post Score", axis=1)
x_testing = x_testing.drop("Post Comments", axis=1)
y_testing = testing["Post Score"]

################

x_train = x_training
x_test = x_testing
y_train = y_training
y_test = y_testing

x_train = x_train.drop("Permalink", axis=1)
x_test = x_test.drop("Permalink", axis=1)
x_train = x_train.drop("Post ID", axis=1)
x_test = x_test.drop("Post ID", axis=1)
x_train = x_train.drop("Author ID", axis=1)
x_test = x_test.drop("Author ID", axis=1)
x_train = x_train.drop("Author Name", axis=1)
x_test = x_test.drop("Author Name", axis=1)
x_train = x_train.drop("Post Title", axis=1)
x_test = x_test.drop("Post Title", axis=1)
x_train = x_train.drop("Post Body", axis=1)
x_test = x_test.drop("Post Body", axis=1)
x_train = x_train.drop("Author Month", axis=1)
x_test = x_test.drop("Author Month", axis=1)
x_train = x_train.drop("Author Day", axis=1)
x_test = x_test.drop("Author Day", axis=1)
x_train = x_train.drop("Author Hour", axis=1)
x_test = x_test.drop("Author Hour", axis=1)
x_train = x_train.drop("Author Minute", axis=1)
x_test = x_test.drop("Author Minute", axis=1)
x_train = x_train.drop("Author Second", axis=1)
x_test = x_test.drop("Author Second", axis=1)
x_train = x_train.drop("Author Is Gold", axis=1)
x_test = x_test.drop("Author Is Gold", axis=1)
x_train = x_train.drop("Post NSFW", axis=1)
x_test = x_test.drop("Post NSFW", axis=1)


# Convert NSFW boolean values to integers
# x_train['Post NSFW'] = x_train['Post NSFW'].map({
#     'True' : 1,
#     'False': 0
# })

# x_test['Post NSFW'] = x_test['Post NSFW'].map({
#     'True' : 1,
#     'False': 0
# })

# # Convert Author Is Gold boolean values to integers
# x_train['Author Is Gold'] = x_train['Author Is Gold'].map({
#     'True' : 1,
#     'False': 0
# })

# x_test['Author Is Gold'] = x_test['Author Is Gold'].map({
#     'True' : 1,
#     'False': 0
# })

########

import matplotlib.pyplot as plt

def plot_corr(df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns);

plot_corr(training, 10)


######

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression().fit(x_train, y_train)
linear_model_prediction = linear_model.predict(x_test)
linear_model_r2_score = linear_model.score(x_test, y_test)

print(y_test.head())
print(pd.DataFrame(linear_model_prediction).head())
print(linear_model_r2_score)



#