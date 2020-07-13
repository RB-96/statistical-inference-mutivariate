X = BodyFat;
[U,S,V] = svd(X);
size(U);
size(S);
size(V);
% select domenent features
U1 = U(:,1:50);
S1 = S(1:50,:);
V1 = V;

% new matrix
Z = U1 * S1 * V1'

% check the difference between the created matrix and actual matrix
diff = Z-X;
total_diff = sum(sum(diff))
disp(total_diff)
