# set replicas to 0 clears pods
kubectl --namespace default scale deployment $(kubectl --namespace default get deployment | awk '{print $1}') --replicas 0