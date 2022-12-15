Aim: 
a. To develop a simple vacuum cleaner world with only two locations
  i. Identify precepts and actions
  ii. Comment on rationality of the agent
b. To tabulate PEAS description for the following agents- Part picking robot, Satellite image analysis

An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that 
environment through actuators. This simple idea is illustrated in figure below. The term percept is used to 
refer to the agent’s perceptual inputs at any given instant. An agent’s percept sequence is the complete 
history of everything the agent has ever perceived. Agent’s behaviour is
described by the agent function that maps any given percept sequence to an action. Given an agent to 
experiment with, we can, in principle, construct this table by trying out all possible percept sequences and 
recording which actions the agent does in response. Internally, the agent function for an artificial agent will 
be implemented by an agent program. The agent function is an abstract mathematical description; the agent 
program is a concrete implementation, running within some physical system

![image](https://user-images.githubusercontent.com/57552973/184404562-2467f597-f368-48c8-a916-fd99004657a3.png)


Simple example the vacuum-cleaner world shown in Figure. This world is so simple that we can describe 
everything that happens; it’s also a made-up world, so we can invent many variations. This particular world 
has just two locations: squares A and B. The vacuum agent perceives which square it is in and whether
there is dirt in the square. It can choose to move left, move right, suck up the dirt, or do nothing. One very 
simple agent function is the following: if the current square is dirty, then suck; otherwise, move to the other 
square.

![image](https://user-images.githubusercontent.com/57552973/184404600-ec77005e-8127-483f-ad17-d941cb098666.png)


![image](https://user-images.githubusercontent.com/57552973/184404626-a44f78c5-510b-47fb-ba1f-c9bcf0654312.png)


![image](https://user-images.githubusercontent.com/57552973/184404643-0fc10c95-fd60-4b0b-a85e-616f085a0947.png)

![image](https://user-images.githubusercontent.com/57552973/184405019-c77a3611-3862-41e8-89fa-af5bd778e64e.png)




Output:

![image](https://user-images.githubusercontent.com/57552973/184404969-1e52aed3-0724-44bf-862d-e67a3f1de124.png)


