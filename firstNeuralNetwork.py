import numpy as  numpy

# simplest neural network with one input layer of 4 neurons
# and one output 
# input = [1.0,3.3,2.0,4.5]
# weights = [0.8,0.2,1.5,-1.2]
# bias = 10
# output = input[0]*weights[0]+input[1]*weights[1]+input[2]*weights[2]+input[3]*weights[3] + bias

# print(output)
print("Hello Bro")

# level 1 neural network with 2 input layer and one output layer
# 2nd input layer is going to have 3 neurons
# input = [1.0,3.3,2.0,4.5]
# weights1 = [0.8,0.2,1.5,-1.2]
# weights2= [0.8,0.2,1.5,-1.2]
# weights3 = [0.8,0.2,1.5,-1.2]
# bias = [1.0,2,4]
# # below will give 2nd layer 
# output1 = input[0]*weights1[0]+input[1]*weights1[1]+input[2]*weights1[2]+input[3]*weights1[3] + bias[0]
# output2 = input[0]*weights2[0]+input[1]*weights2[1]+input[2]*weights2[2]+input[3]*weights2[3] + bias[0]
# output3 = input[0]*weights3[0]+input[1]*weights3[1]+input[2]*weights3[2]+input[3]*weights3[3] + bias[0]
# # Take 2nd layer as input 
# input2 = [output1,output2,output3]
# print(input2)
# bias2=2 #bias for 2nd layer
# # use the above weights for example only
# output = input2[0]*weights1[0]+input2[1]*weights1[1]+input2[2]*weights1[2] +bias2
# print(output)

# okay now lets use some numpy for making things simpler
# input = [1.0,3.3,2.2,4.5]
# weights1 = [0.8,0.2,1.4,-1.2]
# weights2= [0.1,0.2,1.2,-1.0]
# weights3 = [0.9,0.2,1.5,-1.4]
# weights = [weights1,weights2,weights3]
# bias = [1.0,2.0,4.0]
# output = numpy.dot(weights,input) + bias
# print(output)
'''

below we will be doing this operaton: vector(1D Array)* matrix multiplication

this output can be given to next hidden layer as input 
weights2 = [[0.2,4.2,1.3],[4.1,0.9,1.8],[1.5,1.1,0.4]]
bias2 = [3.2,1.0,2.1]
output1 = numpy.dot(weights2,output) + bias2
print(output1)
this can be repeated so on and so forth...

Now what i want is to give batch of input with the same weights so that
we can do things faster

i.e inputs = [[1.0,3.3,2.2,4.5],
            [1.0,3.1,1.3,3.1],
            [1.4,3.2,2.1,2.1],
            [1.9,1.1,3.2,1.1]]
so
'''
# inputs = [[1.0,3.3,2.2,4.5],
#             [1.0,3.1,1.3,3.1],
#             [1.9,1.1,3.2,1.1]]
# weights1 = [0.8,0.2,1.4,-1.2]
# weights2= [0.1,0.2,1.2,-1.0]
# weights3 = [0.9,0.2,1.5,-1.4]
# weights = [weights1,weights2,weights3]
# bias = [1.0,2.0,4.0]

# # this wont work as now it tries to do cross multiplication(matrix*matrix) rather than vector*matrix multiplication
# #  [1.0,3.3,2.2,4.5]    [0.8,0.2,1.4,-1.2]        you know cross  multiplication rule:
# #  [1.0,3.1,1.3,3.1] *  [0.1,0.2,1.2,-1.0]                      3*4 = 4*3 and not 3*4=3*4
# #  [1.4,3.2,2.1,2.1]    [0.9,0.2,1.5,-1.4]
# #                  3*4                  3*4
# # output = numpy.dot(inputs,weights)+bias
# # so we will need to transpose the weights to meet out requirements
# output = numpy.dot(inputs,numpy.transpose(weights))+ bias
# similarly this output can be given to input for next layers
# # the output of above cross multiplication will be : 
# # [[0.14 0.9  2.56]  batch1
# #  [0.52 1.18 3.13]  batch2
# #  [5.9  5.15 9.19]] batch3
# print(output)

# now lets make things real

# numpy.random.seed(0)
# X = [[1.0,3.3,2.2,4.5],
#     [1.0,3.1,1.3,3.1],
#     [1.9,1.1,3.2,1.1]]
# class Layer_dense:
#     # constructor
#     def __init__(self,n_inputs,n_neurons):
#         # getting weights randomly. i.e for 4 inputs and 3(neurons inside layers) output we want 12 weights
#         self.weights = 0.10*numpy.random.randn(n_inputs,n_neurons) #randn make shapes out of given params but 
#         # print(self.weights)                                   # but numpy.zero doesnt

#         # self.baises = numpy.zeros(n_neurons) # no of bias depends on no of neurons in inner layer
#         self.baises = numpy.zeros((1,n_neurons)) # (1,n_neurons) this is to define the shape
#         # print(self.baises)
#     # method
#     def forward(self,inputs):
#         # for inputs neurons we want to generate output layer 
#         self.output = numpy.dot(inputs,self.weights)+self.baises
#         return self.output

# #lets create a layer now
# layer1 = Layer_dense(4,3) # with 4 inputs and 3 outputs
# # print(layer1.weights)
# #  the weights we get is           [[ 1.76405235  0.40015721  0.97873798]
# #                                     [ 2.2408932   1.86755799 -0.97727788]
# #                                     [ 0.95008842 -0.15135721 -0.10321885]
# #                                     [ 0.4105985   0.14404357  1.45427351]]
# output1 = layer1.forward(X)
# layer2 = Layer_dense(3,2)
# output2 =layer2.forward(output1)
# print("Layer 1 output is :",output1)
# print("Layer 2 output is :",output2)

# okay this looks great. we have successfully created hidden layers

# now lets talk about activation functions
# the ones tha we know are ReLu, Sigmoid(Logistic), Linear
# The activation function compares the input value to a threshold value. 
# If the input value is greater than the threshold value, the neuron is activated.
# lets do ReLu
# relu function is if x> 0 return x
#                   if x<=0 return 0
numpy.random.seed(0)
X = [[1.0,-3.3,2.2,4.5],
    [1.0,3.1,1.3,-3.1],
    [1.9,-1.1,-3.2,1.1]]
class Layer_dense:
    # constructor
    def __init__(self,n_inputs,n_neurons):
        # getting weights randomly. i.e for 4 inputs and 3(neurons inside layers) output we want 12 weights
        self.weights = 0.10*numpy.random.randn(n_inputs,n_neurons) #randn make shapes out of given params but 
        # print(self.weights)                                   # but numpy.zero doesnt

        # self.baises = numpy.zeros(n_neurons) # no of bias depends on no of neurons in inner layer
        self.baises = numpy.zeros((1,n_neurons)) # (1,n_neurons) this is to define the shape
        # print(self.baises)
    # method
    def forward(self,inputs):
        # for inputs neurons we want to generate output layer 
        self.output = numpy.dot(inputs,self.weights)+self.baises
        return self.output
class ReLu_activation:
    def forward(self,inputs):
            self.output = numpy.maximum(0,inputs) # if the value is less than 1, max is of (0,0) or (0,-10) else value is input val
            return self.output
            # or we could also do 
            # output = []
            # for input in inputs:
            #     if(input>0):
            #           output.append(input)
            #     elif(input<=0):
            #          output.append(0)
                    


layer1 = Layer_dense(4,3) # with 4 inputs and 3 outputs
output1 =layer1.forward(X)
activation1 = ReLu_activation()
activation1.forward(output1)
print(activation1.output)

# layer2 = Layer_dense(3,2)
# output2 =layer2.forward(output1)
print("Layer 1 output is :",output1)
# print("Layer 2 output is :",output2)


# ReLu is having problem here. What if the input is -20,-1? both will have 0 as output
# this doesnt seem much reliable 
# we can use exponential function e^x that narrow down the negative values to nearby zero
# without loosing the value of that number. if x= -10 e^x = 0.00005, x=-4.7 = 0.0032...
# but again we get problem for positive number  if x = 10 , e^x = 22,000 (very high)
# to narrow down that higher value what we can do is subtract all the values of input from the highest
# this make the highest value as 0(highest-highest) i.2 e^0 is 1 (this is known as overflow prevention)
# this will give values between -inf and 1 for any kind of input

class SoftMax_activation:
     def forward(self,input):
          maxi =  numpy.max(input,axis=1,keepdims=True)
          exp_values = numpy.exp(input - maxi)
          norm_sum = numpy.sum(exp_values,axis=1,keepdims=True)
          self.output = exp_values/norm_sum
        
          print(self.output)

softact = SoftMax_activation()
softact.forward(X)