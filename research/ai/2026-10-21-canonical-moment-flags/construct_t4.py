"""Reconstruct the small integer canonical T4 maps from block factors."""
import argparse,json
from pathlib import Path

def construct():
    m,a,b=4,5,10
    factors=[
        [0,0,0,0,0,0,0,0,1,-1],
        [1,0,0,0,0,-1,0,0,-1],
        [0,0,0,1,-1,0,0,0],
        [1,0,0,-1,0,0,-1]]
    moments=[
        [-2,-2,-2,-1,-1,-1,-1,-1,-1,-1,-1,0,0,0],
        [6,6,5,4,4,4,4,3,2,2,2,2,2,2,2],
        [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,2,2,2,2,1,0,0,0,0]]
    A=[[0,0,0,0,1],[0,0,0,1,-1],[-1,1,0,0,0],[1,0,0,0,0]]
    Y=[];Z=[]
    for p in range(m):
        g=factors[p]
        for k in range(p+1):
            Y.append([g[j-k] if 0<=j-k<len(g) else 0 for j in range(b)])
            Z.append(moments[p][k:k+a+b-1])
    return {"source":[a,b],"m":m,"target":"canonical T4","a_map":A,"y":Y,"z":Z,
            "block_factors":factors,"block_moments":moments,
            "weights_x":[-3]*m,"weights_y":[p for p in range(m) for _ in range(p+1)],
            "weights_z":[p for p in range(m) for _ in range(p+1)],
            "coefficient_ring":"integers","improves_omega":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    args.output.write_text(json.dumps(construct(),indent=2)+"\n")
