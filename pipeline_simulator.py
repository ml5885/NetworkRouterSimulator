pipelineCounter = 0

def parallel_pipeline():
	global pipelineCounter
	pipelineCounter = 0
	pipelineCounter1 = pipelineCounter
	time = 0
	packet1 = "b"
	packet2 = "b"

	def stage1(packet, pipelineCounter2):
		if packet1 == "b": 
			return pipelineCounter2 + 1

	def stage2(packet):
		return packet

	pipelineCounter1 = stage1(packet1, pipelineCounter)
	pipelineCounter1 = stage1(packet2, pipelineCounter)
	pipelineCounter = pipelineCounter1
	time += 1
	stage2(packet1)
	stage2(packet2)
	time += 1

	print(time);
	print("Parallel Pipeline: " + str(pipelineCounter))
	return pipelineCounter

def single_pipeline():
	global pipelineCounter
	pipelineCounter = 0
	time = 0
	packet1 = "b"
	packet2 = "b"

	def stage1(packet):
		global pipelineCounter
		if packet == "b":
			pipelineCounter += 1

	def stage2(packet):
		return packet

	stage1(packet1)
	time += 1
	stage1(packet2)
	stage2(packet1)
	time += 1
	stage2(packet2)
	time += 1

	print(time)
	print("Single Pipeline: " + str(pipelineCounter))
	return pipelineCounter

counter = single_pipeline()	
counter1 = parallel_pipeline()

if counter == counter1:
	print("Function equivalence was achieved!")
else:
	print("Functional equivalence was not achieved")
