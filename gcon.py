#    Copyright (C) 2019 Greenweaves Software Limited
#
#    This is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This software is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>

# GCON Global Alignment with Constant Gap Penalty

from align import align

def get_indel_cost_with_skips(sigma,delta,i,j,di,dj,moves):
    i_previous = i+di
    j_previous = j+dj
    
    if (i_previous,j_previous) in moves:
        _,_,di_previous,dj_previous = moves[(i_previous,j_previous)]
        if (di_previous==0 and di==0) or (dj_previous==0 and dj==0):
            return di+di_previous,dj+dj_previous,sigma

    return di,dj,sigma

def get_score(s,t,matrix,moves,showPath=False):
    return matrix[len(s)][len(t)],[],[]

if __name__=='__main__':
    from Bio.SubsMat.MatrixInfo import blosum62
    from Bio import SeqIO
    import sys,os
    if sys.argv[1]=='--sample':
        score,_,_=align('PLEASANTLY','MEANLY',
                            replace_score=blosum62,
                            indel_cost=(5,0),
                            get_indel_cost=get_indel_cost_with_skips,
                            backtrack=get_score,
                            showScores=False,showPath=False)
        print (score)
    elif sys.argv[1]=='--test':
        name,_ = os.path.splitext(os.path.basename(sys.argv[0]))
        if len(sys.argv)>2:
            name = name + '({0})'.format(int(sys.argv[2])) 
        with open(os.path.join(r'C:\Users\Simon\Downloads','rosalind_{0}.txt'.format(name)),'r') as f:
            print ('Processing {0}'.format(f.name))
            strings = [] 
            for record in SeqIO.parse(f,'fasta'):
                print (record.id)
                print (str(record.seq))
                strings.append(str(record.seq))    
            score,_,_=align(strings[0],strings[1],
                            replace_score=blosum62,
                            indel_cost=(5,0),
                            get_indel_cost=get_indel_cost_with_skips,
                            backtrack=get_score,
                            showScores=False,showPath=False)
            print (score)
    else:
        score,_,_=align(sys.argv[1],sys.argv[2],
                        replace_score=blosum62,
                        indel_cost=(5,0),
                        get_indel_cost=get_indel_cost_with_skips,
                        backtrack=get_score,
                        showScores=False,showPath=False)
        print (score)         
