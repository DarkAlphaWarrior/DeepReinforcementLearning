#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:46:25 2019

@author: alex
"""

import numpy as np
from dqn_keras import Agent
from utils import plotLearning,make_env

if __name__ == '__main__':
    env = make_env('PongNoFramesskip-v4')
    num_games = 250
    load_checkpoint = False
    best_score = -21
    
    agent = Agent(gamma=0.99,epsilon=1.0,alpha=0.0001,inputs_dims=(4,80,80),
                  n_actions=6, mem_size=25000,eps_min=0.02,batch_size=32,
                  replace=1000,eps_dec=1e-5)
    if load_checkpoint:
        agent.load_models()
        
        filename = 'PongNoFrameSkip-v4.png'
        
        scores, eps_history = [], []
        n_steps = 0
        
        for i in range(num_games):
            score = 0
            observation = env.reset()
            done = False
            while not done:
                action = agent.choose_actiom(observation)
                observation_,reward,done,info = env.step(action)
                n_steps +=1
                score += reward
                if not load_checkpoint:
                    agent.store_transition(observation, action,
                                           reward,observation_,int(done))
                    agent.learn()
                
                else:
                    env.render()
            
                observation = observation_
            scores.append(score)
            
            avr_score = np.mean(scores[-100:])
            print('episode',i,'score',score,
                  'average score %.2f' % avg_score, 'epsilon %.2f' % agent.epsilon,
                  'steps',n_steps)
            
            if avg_score > best_score:
                agent.sve_models()
                print('avg score %.2f better than bestscore %.2f' %
                         (avg_score,best_score))
                best_score = avg_score
            
            eps_history.append(agent.epsilon)
        X = [i+1 for i in range(num_games)]
        plotLearning(x,scores,eps_history,filename)
        
            
                
                
                
                 
    