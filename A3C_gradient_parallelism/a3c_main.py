from a3c_learn import A3Cagent

def main():
    max_episode_num = 1000
    env_name = 'Pendulum-v1'
    agent = A3Cagent(env_name)

    agent.train(max_episode_num)

    agent.plot_result()
if __name__ == "__main__":
    main()