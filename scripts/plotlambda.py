import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Test CurveFitting start...
# iter: 0 , chi= 36048.3 , Lambda= 0.001
# 0.376376 0.460675 0.609312
# iter: 1 , chi= 30015.5 , Lambda= 699.051
# 0.406934 0.476082 0.577158
# iter: 2 , chi= 13421.2 , Lambda= 1864.14
# 0.559701 0.534093 0.367426
# iter: 3 , chi= 7273.96 , Lambda= 1242.76
# 0.00130277  -0.054431  -0.251545
# iter: 4 , chi= 269.255 , Lambda= 414.252
# 0.0224125 0.0362776 -0.105473
# iter: 5 , chi= 105.473 , Lambda= 138.084
# -0.0385961   0.087607 -0.0482162
# iter: 6 , chi= 100.845 , Lambda= 46.028
# -0.114678  0.165734  -0.05535
# iter: 7 , chi= 95.9439 , Lambda= 15.3427
#  -0.149215   0.212627 -0.0694003
# iter: 8 , chi= 92.3017 , Lambda= 5.11423
# -0.0946861   0.135901 -0.0449265
# iter: 9 , chi= 91.442 , Lambda= 1.70474
# -0.0250964  0.0362999 -0.0121585
# iter: 10 , chi= 91.3963 , Lambda= 0.568247
# -0.00251669   0.0036643 -0.00124003
# iter: 11 , chi= 91.3959 , Lambda= 0.378832
# problem solve cost: 0.69831 ms
#    makeHessian cost: 0.392399 ms
# -------After optimization, we got these parameters :
# 0.941939  2.09453 0.965586
# -------ground truth: 
# 1.0,  2.0,  1.0

class PlotLamba(object):
    def __init__(self):
        self.lambdas = [0.001, 699.051, 1864.14, 1242.76,414.252, 138.084,46.028, 15.3427,5.11423,1.70474,0.378832]
        return 
    def run(self):
        plt.plot(np.arange(0, len(self.lambdas)), self.lambdas)
        plt.title("lambda trend")
        plt.show()
        
        return


if __name__ == "__main__":   
    obj= PlotLamba()
    obj.run()
    
    

    