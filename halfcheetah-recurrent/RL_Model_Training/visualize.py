#Visualize and save the plots of the data benchmarks


import pickle

data_ts_folder = 'data'

data_dr_folder = 'data'

saved_models_ts = ['TS1']
saved_models_dr = ['DR1']

#uncomment below for plotting data with 3 or similarly more train checkpoints
#that are benchmarked
#saved_models_ts = ['TS1', 'TS2', 'TS3']
#saved_models_dr = ['DR1', 'DR2', 'DR3']



latencies = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
samplings = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]



#latencies index saved with these names

All_Data = []

#TS first then DR for all models for each latency is loaded
All_Data = []

for i in range(len(latencies)):

    #TS data
    Data = []
    for models in saved_models_ts:
        path = data_ts_folder+'/'+models+'_'+str(samplings[i])+'_'+str(latencies[i])+'.p'
        #print(path)
        data = pickle.load( open( path, "rb" ))
        data = data[0]

        Data = Data + data

    All_Data.append(Data)

    #DR data
    Data = []
    for models in saved_models_dr:
        path = data_dr_folder+'/'+models+'_'+str(samplings[i])+'_'+str(latencies[i])+'.p'
        data = pickle.load( open( path, "rb" ))
        data = data[0]

        Data = Data + data

    All_Data.append(Data)



from matplotlib import pyplot as plt
boxprops = dict(linewidth=1, color='darkgoldenrod')

meanprops = dict(linewidth=1, marker='D')
medianprops = dict(linewidth=1, marker='x', color = 'black')


fig5, ax5 = plt.subplots(figsize=(10,15))

plt.rcParams.update({'font.size': 18})

#order latency 0 is first, and then later
data = All_Data

#bplot1 = ax5.boxplot(data, widths=0.2, vert=False, showfliers=False,boxprops= boxprops, meanprops = meanprops, medianprops = medianprops, showcaps=True, showmeans=True, meanline = True, whis=1.0)
bplot1 = ax5.boxplot(data, widths=0.2, vert=False, showfliers=False,boxprops= boxprops, medianprops = medianprops, showcaps=True, whis=1.0)


# fill with colors
colors = ['blue', 'darkorange']

i = 0
for bplot in (bplot1['boxes']):
    if i%2 ==0:
        bplot.set_c(colors[0])

    else:
        bplot.set_c(colors[1])

    i = i+1
    #for patch, color in zip(bplot['boxes'], colors):
        #patch.set_facecolor(color)

for bplot in (bplot1['means']):
    #print(bplot)
    bplot.set_linestyle('-')

ax5.legend([bplot1["boxes"][0], bplot1["boxes"][1]], ['TS', 'DR'], loc='lower right',fontsize = 30)

ax5.set_yticklabels([ 41.20, 41.20, 37.08, 37.08, 32.96, 32.96, 28.84, 28.84, 24.72, 24.72, 20.60, 20.60,
                     16.48, 16.48, 12.36, 12.36, 8.24, 8.24, 4.12, 4.12, 0, 0
                    ], fontsize = 25,  rotation='0')


plt.grid(True)
plt.xlabel('Episode reward', fontsize=30)
plt.ylabel('Execution Latency ($\Delta\\tau_\eta$) (ms)', fontsize=30)
plt.savefig('visualization.png')
plt.show()
