randP = randi([-10, 10], [4, 4], "uint8")
Q = transpose([ 0 0 1 0; 1 0 0 0 ])
lamdas = [-1 -1 -1 -1]

% randP = [1 -2 2; -1 2 -1; 1 1 0]
% Q = transpose([0 0 1])
% lamdas = [-1 -2 -3]

randP = [0 0 0 1; 0 -1 1 0; 1 -1 0 0; 1 0 0 0]
Q = transpose([0 0 1 0; 1 0 0 0])
lamdas = [-1 -1 -1 -1]


save rand_stabilisation.mat randP Q lamdas -v7.3
