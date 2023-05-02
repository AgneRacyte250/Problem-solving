import matplotlib.pyplot as plt
import csv
def read_data():
    with open('temps.csv') as f:
        reader = csv.reader(f)
        next(reader)
        dict = {'week1':[], 'week2': []}
        for row in reader:
            dict['week1'].append(row[0])
            dict['week2'].append(row[1])
        return dict
def run():
    data = read_data()
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)

    ax1.plot(range(1,8),data['week1'],'r^--')
    ax2.plot(range(1,8),data['week2'], 'bx--')
    plt.show()
run()



