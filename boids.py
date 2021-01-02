#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:08:39 2020

@author: tarnjotbains
"""

import numpy as np
import numpy.random as rnd 

class BoidSim: 
    """
    A class that represents a simulated flock of boids in 2D. 
    
    Attributes
    ----------
    num_boids: int
        Total number of boids in the flock. 
    
    boids: numpy.ndarray
        An array of boid positions.
        
    velocities: numpy.ndarray
        An array of velocities for boids in corressponding boid positions.
        
    """    
    def __init__(self,num_boids: int):
        """
        Generates a flock of boids at randomized start positions and velocities.

        Parameters
        ----------
        num_boids : int
            Number of boids in the flock.

        Returns
        -------
        None.

        """
        self.num_boids = num_boids
        self.boids = self.initialize_positions() 
        self.velocities = self.initialize_velocities() 
        
    def initialize_positions(self): 
        """
        Initializes boids in randomized starting positions. 

        Returns
        -------
        positions : numpy.ndarray
            A float array of boid positions.

        """
        #x and y are coordinate positions. 
        x = rnd.randint(-1 * self.num_boids * 5, self.num_boids * 5,
                        size=(self.num_boids, 1))
        y = rnd.randint(-1 * self.num_boids * 5, self.num_boids * 5, 
                        size=(self.num_boids, 1))
        
        x = x.astype(np.float64)
        rnd.shuffle(x)
        y = y.astype(np.float64)
        rnd.shuffle(y)
        
        positions = np.append(x, y, axis = 1) 
        return positions
    
    def initialize_velocities(self): 
        """
        Initializes randomized velocities of boids in corressponding positions.

        Returns
        -------
        velocity : numpy.ndarray
            A float array of velocities for boids in corresponding boid 
            positions.

        """
        velocity = rnd.uniform(low=-10, high = 10, 
                               size = (self.num_boids,2))
        velocity = velocity.astype(np.float64)
        return velocity
    
    def move_all_boids_to_new_positions(self): 
        """
        Applies boids algorithm and generates new positions and velocities.

        Returns
        -------
        None.

        """
        boids = self.boids
        velocities = self.velocities
        
        for boid_num in range(0,self.num_boids): 
            v1= self.cohesion(boid_num) 
            v2= self.seperation(boid_num) 
            v3 = self.alignment(boid_num) 
            v4 = self.bound_position(boid_num)
        
            velocities[boid_num]+= v1 + v2+ v3 + v4 #update velocity
            velocities[boid_num] = self.limit_velocity(boid_num) #limit velocity
            
            boids[boid_num] += velocities[boid_num] #update position
        
    def limit_velocity(self, boid_num: int):
        """
        Limits the magnitude of a boid's velocity if it exceeds a specified
        magnitude. The boid lies on index boidNum within boids. 

        Parameters
        ----------
        boid_num : int
            The index of a boid.

        Returns
        -------
        boid_velocity : numpy.ndarray
            The velocity of a boid. 

        """
        boid_velocity = self.velocities[boid_num]
        vlim = 50 #The velocity limit. 
        
        if np.linalg.norm(boid_velocity) > vlim :
            boid_velocity = (((boid_velocity) / np.linalg.norm(boid_velocity)) 
                            * vlim)
        return boid_velocity
        
    
    def cohesion(self,boid_num:int):
        """
        Moves boid with index boidNum towards the centre of mass of nearby 
        boids. 

        Parameters
        ----------
        boid_num  : int
            The index of a boid.

        Returns
        -------
        centre_offset: numpy.ndarray
            A vector offset 1% towards the centre of mass of other boids near 
            boid.

        """
        preceived_centre = self.get_closest_boids(boid_num)
        preceived_centre = np.mean(preceived_centre, axis = 0) 
        centre_offset = (preceived_centre  - self.boids[boid_num]) / 100
        return centre_offset


    def seperation(self,boid_num: int): 
        """
        Ensures that boid at index boidNum keeps a distance of atleast 20 units
        away from other boids. 

        Parameters
        ----------
        boid_num : int
            The index of a boid.

        Returns
        -------
        c : int
            Displacement vector of nearby boids.

        """
        c = np.zeros(self.boids[boid_num].shape)
    
        for i in range(0,self.num_boids):
            if i != boid_num: 
                if np.linalg.norm(self.boids[i] - self.boids[boid_num]) < 20: 
                    c -= (self.boids[i]-self.boids[boid_num])
        return c 
                
                
    def alignment(self, boid_num: int):
        """
        Moves the velocity of boid at index boidNum towards the average velocity 
        of all boids. 

        Parameters
        ----------
        boid_num : int
            The index of a boid.

        Returns
        -------
        velocity_offset: numpy.ndarray
            A vector offset 1/8th of boid velocities. 
        
        """
        preceived_velocity = np.sum(self.velocities, axis = 0)
        preceived_velocity -= self.velocities[boid_num] 
        preceived_velocity = preceived_velocity / (self.num_boids-1) 
        
        velocity_offset = (preceived_velocity - self.velocities[boid_num]) / 8
        return velocity_offset
    
    def get_closest_boids(self,boid_num: int): 
        """
        Generates an array of boids that are less than 30 units in distance
        from boid at index boidNum. 

        Parameters
        ----------
        boid_num: int
            The index of a boid.

        Returns
        -------
        closest_array : numpy.ndarray
            an array of boids that are less than 30 units in distance from 
            'boid'. 

        """
        closest_boids = [] # a list of closest boids.
        closest_boids.append(self.boids[boid_num]) 
        closest_boids[0] = closest_boids[0] - self.boids[boid_num] 
    
        for i in range(0,self.num_boids):
            if i != boid_num: 
                if np.linalg.norm(self.boids[i] - self.boids[boid_num]) < 30: 
                    closest_boids.append(self.boids[i])
                
        #convert list to array.         
        closest_array = np.asarray(closest_boids).reshape((len(closest_boids),2))
        return closest_array
    
    
    def bound_position(self, boid_num: int): 
        """
         A rule that encourages boids to stay within a certain area.         

        Parameters
        ----------
        boid_num : int
            The index of a boid.

        Returns
        -------
        bound_displacement: numpy.ndarray
            A displacement vector that encourages boid to remain in a certain
            area upon the next position update. 

        """
        x_min = -1 * self.num_boids * 5
        x_max = self.num_boids * 5
        y_min = -1 * self.num_boids * 5
        y_max = self.num_boids * 5
        bound_displacement = np.zeros(shape= self.boids[boid_num].shape) 
    
        if self.boids[boid_num][0] < x_min:
            bound_displacement[0] = 10
        if self.boids[boid_num][0] > x_max: 
            bound_displacement[0] = -10 
        if self.boids[boid_num][1] < y_min: 
            bound_displacement[1] = 10
        if self.boids[boid_num][1] > y_max: 
            bound_displacement[1] = -10
        
        return bound_displacement
    

        

            
        

            
            
        
        
        