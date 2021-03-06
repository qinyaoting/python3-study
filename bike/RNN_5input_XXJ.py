import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from numpy import shape
import matplotlib.ticker as ticker
'''
遗留问题:

I II III IV V VI VII
1. 画图 &
2. 保存模型文件, 下次直接读取模型
3. 那个维度是用来验证结果 发电量 &
4. 怎么实际给一个值,来获得预测值
5. Mean absolute error: 0.147 Root mean squared error: 0.224   
    平均绝对误差（MAE）损失函数 均方根误差

6. time_step &

'''

"""
Load data into pandas
"""
df = pd.read_csv('WindPower2012.csv', error_bad_lines=False)
print("Length of original data : ", len(df))

# calculate the mean value for every hour and save as a new dataframe
# 每隔5分钟收集一次数据, 一个小时收集12次, 把12次合并到每小时计算平均值
data2 = []
for i in range(len(df) // 12):
    data2.append(df[i * 12:(i + 1) * 12].mean())
data2 = pd.DataFrame(data2)
print("Length of hourly averaged data : ", len(data2))

# Get the values of the 6-11 columns
# 取5到10列, 共6列数据 发电量 风向 风速 气温 气压 密度 index=0 1 2 3 4 5
data = data2.iloc[:, 5:11].values

"""
Set Parameters:
Next we set the RNN model parameters. We will run the data through 20 epochs, in batch sizes of 14.
The RNN will be of size 10 units.   
"""
rnn_unit = 10  # hidden layer units
input_size = 5  # 对应用于训练模型的5列数据, 另外一列是测试结果用的
output_size = 1
lr = 0.0006  # learning rate

batch_size = 14     # 每批14条记录
time_step = 6       # LSTM 认为每个输入数据与前多少个陆续输入的数据有联系

train_begin = 0
train_end = 6000
test_begin = 6000
test_len = 180
iter_time = 100

# RNN output node weights and biases
weights = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}

biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
}

"""
Preparing the training data   
"""


# Get train data function: load training data for LSTM
# Input: batch_size, time_step, train_begin, train_end
# Output: batch_index, train_x, train_y

def get_train_data(batch_size, time_step, train_begin, train_end):
    batch_index = []

    # normalize the data
    # 标准化
    scaler_for_x = MinMaxScaler(feature_range=(0, 1))
    # 把数据缩放到0到1
    scaled_x_data = scaler_for_x.fit_transform(data)

    scaler_for_y = MinMaxScaler(feature_range=(0, 1))
    # 取第一列(发电量)为y_data
    # scaled_y_data = scaler_for_y.fit_transform(data[:, 0].reshape(-1, 1))   #?2&

    # get train data
    # 0-6000为训练集,共8784条记录
    normalized_train_data = scaled_x_data[train_begin:train_end]
    train_x, train_y = [], []
    for i in range(len(normalized_train_data) - time_step):
        if i % batch_size == 0:
            batch_index.append(i)
        # x是把normalized_train_data分成好几批, 往后错1
        x = normalized_train_data[i:i + time_step, 1:6]     #?1
        # y是取i的下一行第一列(发电量),作为模型验证的值
        y = normalized_train_data[i + 1:i + time_step + 1, 0, np.newaxis]
        train_x.append(x.tolist())
        train_y.append(y.tolist())
    batch_index.append((len(normalized_train_data) - time_step))
    return batch_index, train_x, train_y


"""
Preparing the testing data   
"""


# Get test data function: load testing data for LSTM
# Input: time_step, test_begin, test_len
# Output: test_x, test_y, scaler_for_x, scaler_for_y

def get_test_data(time_step, test_begin, test_len):
    # normalize the data
    scaler_for_x = MinMaxScaler(feature_range=(0, 1))
    scaler_for_y = MinMaxScaler(feature_range=(0, 1))
    scaled_x_data = scaler_for_x.fit_transform(data)
    scaled_y_data = scaler_for_y.fit_transform(data[:, 0].reshape(-1, 1))

    # get test data
    size = test_len // time_step
    # 取的6000-6180行为测试集
    normalized_test_data = scaled_x_data[test_begin: (test_begin + test_len)]
    normalized_test_lable = scaled_x_data[test_begin + 1: (test_begin + test_len + 1)]
    test_y = normalized_test_lable[:, 0]
    # 把测试集 分成几段
    test_x = []
    for i in range(size):
        x = normalized_test_data[i * time_step:(i + 1) * time_step, 1:6]
        test_x.append(x.tolist())
    return test_x, test_y, scaler_for_x, scaler_for_y


"""
Creating the LSTM network   
"""


# LSTM function: definition of recurrent neural network
# Input: X
# Output: pred, final_states

def lstm(X):
    batch_size = tf.shape(X)[0]
    time_step = tf.shape(X)[1]
    w_in = weights['in']
    b_in = biases['in']

    # reshape to (batch_size * time_step, input_size)
    input = tf.reshape(X, [-1, input_size])  # turn tensor to 3D-Array as the input of hidden layer
    input_rnn = tf.matmul(input, w_in) + b_in
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])

    # create an LSTM cell to be unrolled
    cell = tf.contrib.rnn.BasicLSTMCell(rnn_unit)
    # cell=tf.contrib.rnn.core_rnn_cell.BasicLSTMCell(rnn_unit)
    # cell=tf.nn.rnn_cell.BasicLSTMCell(rnn_unit)

    # At each time step, reinitialising the hidden state
    init_state = cell.zero_state(batch_size, dtype=tf.float32)

    # generate prediction
    # create a dynamic RNN object in TensorFlow.
    # This object will dynamically perform the unrolling of the LSTM cell over each time step
    output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state,
                                                 dtype=tf.float32)

    output = tf.reshape(output_rnn, [-1, rnn_unit])
    w_out = weights['out']
    b_out = biases['out']
    ## Get the last output
    pred = tf.matmul(output, w_out) + b_out
    return pred, final_states


"""
Training the LSTM Model and Making Predictions   
"""


# train_lstm function: train the LSTM model, make predictions, and calculate the error of predication
# Input: batch_size, time_step, train_begin, train_end, test_begin, iter_time, test_len
# Output: test_y, test_predict, loss_list, rmse, mae

def train_lstm(batch_size, time_step, train_begin, train_end, test_begin, iter_time, test_len):
    # set up the state storage / extraction
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    Y = tf.placeholder(tf.float32, shape=[None, time_step, output_size])
    batch_index, train_x, train_y = get_train_data(batch_size, time_step, train_begin, train_end)

    print("Training parameters:***************************************************")
    print("batch size: ", batch_size)
    print("Number of batches: ", len(batch_index))
    print("Shape of training samples:", shape(train_x))
    print("Shape of training labels:", shape(train_y))

    pred, _ = lstm(X)

    ## Loss and optimizer
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1]) - tf.reshape(Y, [-1])))
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)
    loss_list = []
    print("Training begins: *****************************************************")

    ## Training step optimization
    """
    The loss are accumulated to monitor the progress of the training. 
    20 iteration is generally enough to achieve an acceptable accuracy.
    """
    # saver = tf.train.Saver()
    with tf.Session() as sess:
        # Initializing the variables
        sess.run(tf.global_variables_initializer())
        # saver.restore(sess, "save/model.ckpt")
        # repeat training 50 times
        for epoch in range(iter_time):
            for step in range(len(batch_index) - 2):
                ## Calculate batch loss
                _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[batch_index[step]:batch_index[step + 1]],
                                                                 Y: np.array(
                                                                     train_y[batch_index[step]:batch_index[step + 1]],
                                                                     dtype=float).reshape(batch_size, time_step, 1)})
                loss_list.append(loss_)

            # Show loss every 5 iterations
            if epoch % 5 == 0:
                print("Epoch:", epoch, " loss:", loss_)

                # if step%100==0:
                # print('Epoch:', epoch, 'steps: ', step,  'loss:', loss_)
        print("Training Optimization Finished! ***************************************")
        #
        # saver.save(sess, './my-model/model.ckpt', global_step=step, write_meta_graph=False)

        """Testing the model"""
        print("Prediction Begins: ****************************************************")
        test_x, test_y, scaler_for_x, scaler_for_y = get_test_data(time_step, test_begin, test_len)
        print("Shape of testing samples:", shape(test_x))

        test_predict = []
        for step in range(len(test_x)):
            prob = sess.run(pred, feed_dict={X: [test_x[step]]})
            predict = prob.reshape((-1))
            test_predict.extend(predict)
        # test_predict = scaler_for_y.inverse_transform(np.array(test_predict).reshape(-1,1))
        # test_y = scaler_for_y.inverse_transform(np.array(test_y).reshape(-1,1))

        test_y = np.array(test_y).reshape(-1, 1)
        test_predict = np.array(test_predict).reshape(-1, 1)
        print("Shape of testing lables:", shape(test_predict))
        test_predict = scaler_for_y.inverse_transform(test_predict).reshape(-1, 1)
        test_y = scaler_for_y.inverse_transform(test_y).reshape(-1, 1)

        # calculate the error of predication
        rmse = np.sqrt(mean_squared_error(test_predict, test_y))
        mae = mean_absolute_error(y_pred=test_predict, y_true=test_y)
        print("Mean absolute error:", "{:.3f}".format(mae),
              "Root mean squared error:", "{:.3f}".format(rmse))
    return test_y, test_predict, loss_list, rmse, mae


# draw test and diction curve
def draw_picture(test_y, test_predict):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(test_y, label="Real")
    ax.legend(loc='upper left')
    plt.plot(test_predict, label="Prediction")
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    test_y, test_predict, loss_list, rmse, mae = train_lstm(batch_size, time_step, train_begin, train_end, test_begin, iter_time, test_len)
    draw_picture(test_y, test_predict)
