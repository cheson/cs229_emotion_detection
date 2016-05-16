import random
import sys

num_examples = int(sys.argv[1])
labels = [random.randint(1,8) for p in range(0,num_examples)]
f = open('random_labels','w')
f.write(str(labels))
f.close()

