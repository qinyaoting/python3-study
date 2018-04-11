import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.metrics import mean_absolute_error,mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
# % matplotlib inline
import warnings

'''
是要看看怎么读取多个因素的
仍然不通过

相同的代码例子
https://raw.githubusercontent.com/sld880311/arima_lstm/4e8ae205bcbeb1dd1b0c7edc64a6c25e89c9f16d/tf_lstm.py

'''
col_names = ['年', '月', '日',
                   '当日最高气温', '当日最低气温', '当日平均气温',
                   '当日平均湿度', '输出']

data_path = './weather_data.csv'

df = pd.read_csv(data_path, header=-1, names=col_names)
print(df.head())

# 取3到7列
data = df.iloc[:, 3:8].values
print(data)

rnn_unit = 10
input_size = 4
output_size = 1
lr = 0.0006
tf.reset_default_graph()

weights = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}
biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
}


# 分割数据集
def get_data(batch_size=60, time_step=20, train_begin=0, train_end=487):
    batch_index = []
    scaler_x = MinMaxScaler(feature_range=(0, 1)) # 按列做minmax缩放?2&
    scaler_y = MinMaxScaler(feature_range=(0, 1))
    # 去掉一列, 并缩放到 0,1
    scaled_x_data = scaler_x.fit_transform(data[:, :-1])  # ?3&
    scaled_y_data = scaler_y.fit_transform(data[:, :-1])

    label_train = scaled_y_data[train_begin: train_end]
    label_test = scaled_y_data[train_end:]
    normalized_train_data = scaled_x_data[train_begin:train_end]
    normalized_test_data = scaled_x_data[train_end:]

    train_x, train_y = [], []   # 训练集x和y初定义
    for i in range(len(normalized_train_data) - time_step):     # ?4
        if i % batch_size == 0:
            batch_index.append(i)
        x = normalized_train_data[i: i+time_step, :4]
        y = label_train[i: i+time_step, np.newaxis]     #?6

        train_x.append(x.tolist())
        train_y.append(y.tolist())

    batch_index.append(len(normalized_train_data) - time_step)

    size = (len(normalized_test_data) + time_step - 1)//time_step  # ?5
    test_x, test_y = [], []
    for i in range(size - 1):
        x = normalized_test_data[i*time_step: (i+1)*time_step, :4]
        y = label_test[i*time_step: (i+1)*time_step]
        test_x.append(x.tolist())
        test_y.append(y)
    test_x.append((normalized_test_data[(i+1)*time_step:, :4]).tolist())
    test_y.extend((label_test[(i+1)*time_step:]).tolist())
    return batch_index, train_x, train_y,test_x, test_y, scaler_y

def lstm(X):
    batch_size = tf.shape(X)[0]
    time_step = tf.shape(X)[1]
    w_in = weights['in']
    b_in = biases['in']
    input = tf.reshape(X, [-1, input_size])
    input_rnn = tf.matmul(input, w_in) + b_in
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])
    cell = tf.contrib.rnn.BasicLSTMCell(rnn_unit)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)
    output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state, dtype=tf.float32)
    output = tf.reshape(output_rnn, [-1, rnn_unit])
    w_out = weights['out']
    b_out = biases['out']
    pred = tf.matmul(output, w_out) + b_out
    return pred, final_states


def train_lstm(batch_size=80, time_step=15, train_begin=0, train_end=487):
    X = tf.placeholder(tf.float32, shape=[None, time_step, input_size])
    Y = tf.placeholder(tf.float32, shape=[None, time_step, output_size])
    batch_index, train_x, train_y, test_x, test_y, scaler_y = get_data(batch_size, time_step, train_begin, train_end)
    pred, _ = lstm(X)
    #
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1])-tf.reshape(Y, [-1])))

    train_op = tf.train.AdamOptimizer(lr).minimize(loss)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        iter_time = 5000
        for i in range(iter_time):
            for step in range(len(batch_index)-1):
                _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[batch_index[step]:batch_index[step + 1]],
                                                                 Y: np.array(
                                                                     train_y[batch_index[step]:batch_index[step + 1]],
                                                                     dtype=float).reshape(batch_size, time_step, 1)})
                if i % 100 == 0:
                    print('iter', i, 'loss:', loss_)
                test_predict = []
                for step in range(len(test_x)):
                    prob = sess.run(pred, feed_dict={X: [test_x[step]]})
                    predict = prob.reshape((-1))
                    test_predict.extend(predict)

                test_predict = scaler_y.inverse_transform(test_predict)
                test_y = scaler_y.inverse_transform(test_y)
                rmse = np.sqrt(mean_squared_error(test_predict, test_y))
                mae = mean_absolute_error(y_pred=test_predict, y_true=test_y)
                print('mae:', mae, '   rmse:', rmse)
            return test_predict


if __name__ == '__main__':
    test_predict = train_lstm(batch_size=80, time_step=15, train_begin=0, train_end=487)


