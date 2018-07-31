import numpy as np
import scipy.stats 

'''Two calculation steps are required before the sample path's data is saved to a file:

(1) Scaling: Since the AR Table has a 16:9 (x:y) ratio in terms of pixels, it seems appropriate that all of these
graphs should have a x_max:y_max of a 16:9 ratio as well. Based on the entered parameters, the paths can have this ratio.

(2) Measurement Noise: The linspace generated paths through linspace do not have "measured" values. Therefore, noise is added
to the positions before passing information this onto the Kalman Filter for tracking, in order to simulate a more real experience.
'''

class PathCalcs:
  def scale_to(x, y, x_scale, y_scale, scale_factor):
      '''Can only accept positive inputs! (This is why there is the quad1_shift definition.) The scale_to 
      definition will make x_max and y_max equal to (scale_factor)*(x_scale or y_scale).'''

      def quad1_shift(x, y):
          '''This will shift the graph to be entirely enclosed within the first quadrant if not already.'''
          x_min = np.amin(x)
          y_min = np.amin(y)
          if (x_min < 0.0):
              x += -x_min
          if (y_min < 0.0):
              y += -y_min
          return (x, y)

      x, y = quad1_shift(x, y) #x and y are now completely positive
      x_max = np.amax(x)
      y_max = np.amax(y)
      #These nested if loops check (and potentially correct) the scale_factor that x and y should be multiplied by.
      if (((0.985*(scale_factor*x_scale)) >= x_max) or ((1.015*(scale_factor*x_scale)) <= x_max)):
          scale_const_x = (x_scale*scale_factor)/x_max
          x *= scale_const_x
          if (((0.985*(scale_factor*y_scale)) >= y_max) or ((1.015*(scale_factor*y_scale)) <= y_max)):
              scale_const_y = (y_scale*scale_factor)/y_max
              y *= scale_const_y
      else:
          if (((0.985*(scale_factor*y_scale)) >= y_max) or ((1.015*(scale_factor*y_scale)) <= y_max)):
              scale_const_y = (y_scale*scale_factor)/y_max
              y *= scale_const_y

      x_max = np.amax(x) #recalculates the x_max and y_max values based on above changes, if any
      y_max = np.amax(y)
      scale_current = x_max/y_max
      scale_target = x_scale/y_scale
      if (((0.985*(scale_target)) <= scale_current) and ((1.015*(scale_target)) >= scale_current)): #final scale check
          return (x,y)
      else:
          return False
    
  def measurement_noise(x, y, x_scale_uncertainty, y_scale_uncertainty):
    #NOISE OF THE POSITION (i.e. THE MEASURED POSITION): 
    '''Assumption 1: The measured position error from actual position follows a normal distribution; 
       Assumption 2: This error is independent of the object's speed at a given moment in time;
       Note 1: The error's normally distributed scale can be arbitrarily set and selected to what is deemed
       appropriate. It could be adjusted to see the effect it would have on each predictive position method.'''
       
       x_measured = x + scipy.stats.norm.rvs(size = len(x), scale = x_scale_uncertainty)
       y_measured = y + scipy.stats.norm.rvs(size = len(y), scale = y_scale_uncertainty)
       
       position_measured = [list(i) for i in zip(x_measured, y_measured)
       return (position_measured)
