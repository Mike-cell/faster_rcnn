def aop(func):
    """aop func"""
    def wrapper():
        """wrapper func"""
        print('before func')
        func()
        print('after func')
    return wrapper

@aop
def hi():
    """hi func"""
    print('hi')
    
@aop
def hello():
    """hello func"""
    print('hello')




if __name__ == '__main__':

    # import numpy as np
    # mean = np.array([[1 ,2 ,3],[1,2,2]])
    # mean = mean[:, None, None]


    # import torch
    # k = [7,8,9,7,8,7,8,6]
    # for i in range(100):
    #     index = int(torch.empty(1).uniform_(0., float(len(k))).item())
    # a = torch.empty(2, 3)


    hi()
    # hello()