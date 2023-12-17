dt = 0.001;
myData = simout;
time = (0:dt:(length(myData) - 1) * dt)';
dataToSimulink = [time, myData];

assignin('base', 'JelobInput', dataToSimulink)
