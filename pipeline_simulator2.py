import random
import matplotlib.pyplot as plt 
import numpy as np

def parallel_pipeline(numberOfFlows, rateList, numberOfPackets):
    packetList = []
    packetPerFlowList = []
    counter = 0
    packetFlowList = []
    pipelineQueue = []
    time = 0

    for x in rateList:
        packetPerFlowList.append(int(x*numberOfPackets))

    num = 1
    for j in packetPerFlowList:
        for i in range(j):
            packetList.append(num)
        num += 1

    if len(packetList) < numberOfPackets:
        for i in range(numberOfPackets-len(packetList)):
            packetList.append(random.randint(1,numberOfFlows))

    random.shuffle(packetList)

    for i in range(numberOfFlows):
        arr = []
        packetFlowList.append(arr)

    while counter < numberOfPackets:
        # print("Packet List: ", len(packetList))
        nonEmptyFlowList = []

        for i in range(8):
            if packetList:
                index = packetList[0]-1
                packetFlowList[index].append(packetList.pop(0))


        count = False
        for arr in packetFlowList:
            if arr:
                count = True

        if not count and not packetList:
            break
        
        for i in range(numberOfFlows):
            if packetFlowList[i]:
                nonEmptyFlowList.append(packetFlowList[i][0])

        random.shuffle(nonEmptyFlowList)

        num = 0
        if len(nonEmptyFlowList) >= 8:
            for i in range(8):
                index = nonEmptyFlowList[i]
                packetFlowList[index-1].pop(0)
                counter += 1
                num += 1
        else:
            for i in nonEmptyFlowList:
                packetFlowList[i-1].pop(0)
                counter += 1
                num += 1;
        time += 1

        if not packetList and not nonEmptyFlowList and not packetFlowList and counter == numberOfPackets:
            break;
        # print("Non empty Flow List: ", nonEmptyFlowList)
        # # print("Non empty Flow List", len(nonEmptyFlowList))
        # # print("Flow List: ", packetFlowList)
        # print("Packet List: ", len(packetList))
        # print("Counter: ", counter)
        # print("Packets: ", num)
        # print("Packets total: ", counter)
        # print("Time: ", time) 
    return time


# flows = 100
# rateList = np.random.random(flows)
# rateList /= rateList.sum()
# print(rateList)

# print(parallel_pipeline(flows, rateList, 30000))

for i in range(20):
    timeList = []
    rateList = []
    for flows in range(1025):
        if flows != 0:
            rates = np.random.random(flows)
            rates /= rates.sum()
            time = parallel_pipeline(flows, rates, 30000)
            timeList.append(time)
            rateList.append(time*(-1.0/26250) + (1 - 3750*(-1.0/26250)))
            print(flows)


    x1 = list(range(1024)) 
    y1 = timeList
      
    plt.plot(x1, y1)

    plt.xscale('log',basex=2)
    plt.ylim(3750,30000)

    plt.xlabel('Number Of Flows') 
    plt.ylabel('Time') 
      
    plt.title('Time vs. Number Of Flows') 

    plt.savefig('graph__{0}.png'.format(i))

    y2 = rateList
    x2 = list(range(1024))
    plt.plot(x2, y2)

    plt.xscale('log',basex=2)
    plt.ylim(0,1)

    plt.xlabel('Number Of Flows') 
    plt.ylabel('Rate') 
      
    plt.title('Rate vs. Number Of Flows') 

    print(rateList)

    plt.savefig('graph__rate{0}.png'.format(i))

