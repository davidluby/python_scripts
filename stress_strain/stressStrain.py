import numpy as np

# this function calcultes modulus, yield, and ultimate for discrete data

def MYU(x,y,window,tol):
    i = -1
    sX = 0 # initialize sum x
    sY = 0 # initialize sum y
    sXY = 0 # intialize sum x*y
    sXX = 0 # initialize sum x^2

    while i < len(x): # while loop for sliding polynomial fit
        i += 1
        j = i
        while j < window:
            j += 1
            sX += x[j]
            sY += y[j]
            sXY += x[j]*y[j]
            sXX += x[j]**2
        m = (sX*sY - sXY*j)/(sX**2 - sXX*j) # slope across window

        if i == 0: # pass on first run
            old = m
            window += 1
        elif (m-old)/old > -tol: # if %change in slope > -tolerance
            old = m
            window += 1
        else: # if % change in slope < -tolerance
            break
        break

    index = window # index of knee in curve
    
    i = -1
    sX = 0 # initialize sum x
    sY = 0 # initialize sum y
    sXY = 0 # intialize sum x*y
    sXX = 0 # initialize sum x^2

    while i < window: # while loop for polynomial fit across linear region
        i += 1
        sX += x[i]
        sY += y[i]
        sXY += x[i]*y[i]
        sXX += x[i]**2
    modulus = (sX*sY - sXY*i)/(sX**2 - sXX*i)/1000 # modulus elasticity
    
    return(modulus, index, np.argmax(y))