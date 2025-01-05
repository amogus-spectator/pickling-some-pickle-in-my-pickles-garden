from random import *
import matplotlib.pyplot as plt

agent_ids = []
class Agent:
    def __init__(self, local_value, id):
        self.value = int(local_value)
        self.id = id
        self.verify_agent_id()
        self.index = self.get_id_index()
    
    def generate_new_value(self, range_lower_bound, range_upper_bound):
        return randint(int(range_lower_bound), int(range_upper_bound))
    
    def get_value(self):
        return self.value
    
    def get_id(self):
        return self.id
    
    def verify_agent_id(self):
        agent_ids.append(self.id)
    
    def get_id_index(self):
        return agent_ids.index(self.id)
    
    def get_all_info(self):
        return f"Agent {self.id} has value {self.value} at index {self.index}"
    
class Randomizer:
    
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
    def randomize(self):
        return randint(self.lower_bound, self.upper_bound)
    
def generation(agents_generator):
    def div(agents_generator_list, divisor):
        agent_partitions = []
        processing_list = agents_generator_list[:]
        for i in range(len(agents_generator_list) // divisor):
            if not processing_list:
                break
            partition = [processing_list.pop(0)]
            randomizer = Randomizer(0, len(processing_list) - 1)
            while len(partition) < divisor and processing_list:
                random_index = randomizer.randomize()
                if random_index < len(processing_list):
                    partition.append(processing_list.pop(random_index))
            agent_partitions.append(partition)
        if processing_list:
            agent_partitions.append(processing_list)
        return agent_partitions

    agent_pairs = div(agents_generator, 2)

    def comparator(agent1, agent2):
        agent1.generate_new_value(1, 100)
        agent2.generate_new_value(1, 100)
        if agent1.get_value() > agent2.get_value():
            return agent1
        else:
            return agent2
        
    def comparartor_bin(agent1, agent2):
        r = comparator(agent1, agent2)
        if r == 1:
            return 0
        elif r == agent1:
            return 0
        elif r == agent2:
            return 1
        
    def simulate(agents_list):
        simulator_result = []
        while len(agents_list) > 1:
            r = comparator(agents_list[0], agents_list[1])
            if r == 1:
                simulator_result.append(agents_list[0].get_id())
            else:
                simulator_result.append(r.get_id())
        return simulator_result
            
            
    simulator_result = []
    simulator_result_bin = []
    while len(agent_pairs) > 1:
        if len(agent_pairs[0]) == 1:
            simulator_result.append(agent_pairs[0][0].get_id())
            simulator_result_bin.append(0)
            agent_pairs = agent_pairs[1:]
        simulator_result.append(simulate(agent_pairs[0]))
        simulator_result_bin.append(comparartor_bin(agent_pairs[0][0], agent_pairs[0][1]))
        agent_pairs = agent_pairs[1:]
        
    simulator_appended_result = [simulator_result, simulator_result_bin]
    return simulator_appended_result
def main():
    def generate_agents(num_agents, value_range):
        agents = []
        for i in range(num_agents):
            local_value = randint(value_range[0], value_range[1])
            agent = Agent(local_value, f"agent_{i}")
            agents.append(agent)
        return agents
    
    r = generate_agents(4, [1, 100])
    simul_r = []
    while len(r) > 1:
        bypasser = generation(r)
        r = bypasser[0]
        simul_r.append(bypasser[1])
        print(r)
    
    i = 1
    while i < len(simul_r):
        plt.plot(simul_r[i-1], label=f"Generation {i}")
        i += 1
    plt.legend()
    plt.show()
    
    

if __name__ == "__main__":
    main()