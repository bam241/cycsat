from modeler.model import Simulation, Surface, Agent

# must be a list of Surface objects
surfaces = [Surface(np.ones((100, 100), dtype='int8'))]

# a list of Agent objects
agents = [Agent() for x in range(10)]

# times steps
timesteps = pd.date_range('1/1/2015', '1/31/2015')

s = Simulation(surfaces, agents, timesteps)
s.run()
