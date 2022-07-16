import gym 
import numpy as np 
import time

env = gym.make("CartPole-v1")

# def basic_policy(PoleAngle):
#     if PoleAngle < 0: # failing left
#         return 0 # Move left
#     else:
#         return 1

def basic_policy(PoleAngle):
    if PoleAngle < 0: # failing left
        return 0 # Move left
    return 1

total_rewards = list()

N_episodes = 200
N_steps = 200

for episode in range(N_episodes):
    rewards = 0
    # CardPosition, Cart velocity, PoleAngle, PoleAngular velocity - their order is also important
    Observations = env.reset()
    PoleAngle = Observations[2]
    for step in range(N_steps):
        env.render()
        action = basic_policy(PoleAngle)
        Observations, reward, done, info = env.step(action)
        time.sleep(0.001)  # Sleep 
        rewards +=reward
        if done: # Fallen
            breakpoint
    total_rewards.append(rewards)

stats= {
    "mean": np.mean(total_rewards),
    "std" : np.std(total_rewards),
    "min": np.min(total_rewards),
    "max": np.max(total_rewards)
}
print(stats)

